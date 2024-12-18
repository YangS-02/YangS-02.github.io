import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
import scipy.integrate as integrate


tol = 2 * 9e-15
c = 0.6
p = 1000
n = int(p / c)
print(n)

sd_beta = 0.3
sd_x = 16
sd_X = 50
# Y = (beta * x^T) + X
# x:    a n-vector draw from N(0, sigma^2), sigma = 16
x = np.random.normal(0.0, sd_x, size=(n, 1))
# X:    a p * n matrix draw from N(0, d^2), d = 50
X = np.random.normal(0.0, sd_X, size=(p, n))
np.random.seed(1)
# beta: a p-vector draw from N(0, s^2), s = 0.3
beta = np.random.normal(1, sd_beta, size=(p, 1))
Y = np.dot(beta, np.transpose(x)) + X
v2 = sd_X ** 2
a = v2 * (1 - np.sqrt(c)) ** 2
b = v2 * (1 + np.sqrt(c)) ** 2
print("Theoretical:", v2)
print("Sample Variance:", np.var(Y))
print("Sample Mean:", np.mean(Y))
print(f'a = {a:}\nb = {b}')

if c <= 1:
    lams, eigenvector = np.linalg.eigh(Y @ Y.T / n)
    leading = eigenvector[:, -1]
else:
    lams, eigenvector = np.linalg.eigh(Y.T @ Y / n)
    leading = eigenvector[:, -1]
print(lams)


Leading = leading/np.linalg.norm(leading)
beta_Norm = beta/np.linalg.norm(beta)
mean_L = np.mean(Leading)
std_dev_L = np.std(Leading)
skewness_L = skew(np.array(Leading))
kurt_L = kurtosis(Leading)

# The following codes are just trying to figure out a better Theoretical Approximation for the leading eigenvalue
print(f'Leading lambda (Cov) = {(np.linalg.norm(beta) **2 * sd_x ** 2) + sd_X ** 2 - lams[-1]}')
# This is an estimator I found:
print(f'Leading lambda (ECM) = {np.linalg.norm(beta) ** 2 * np.linalg.norm(x) ** 2 /n + sd_X **2}')
# The following is the one found on the book, A First Course in Random Matrix Theory, by Marc Potters:
values_a = ((sd_x ** 2) * (np.linalg.norm(beta) ** 2)) / (sd_X ** 2)
print(f"Leading lambda (ECM2) = {sd_X ** 2 * (1 + values_a) * (1 + (c / a)) - lams[-1]}")


def mc(x):
    x = np.asarray(x)
    mp = np.where((x >= a) & (x <= b) & (x != 0), np.sqrt((b - x) * (x - a)) / (2 * v2 * np.pi * c * x), 0)
    mp = np.where((x == 0) & (c > 1), mp + ((c - 1) / c), mp)
    return mp


pp = len(lams)
lams = np.append(np.zeros(p - pp), lams)
I = integrate.quad(mc, a, b, epsabs=tol)
mass = I[0] + np.maximum(1.0 - 1.0 / c, 0)
print(f"mass = {mass}")
if mass < 1.0 - p * tol:
    print("Warning! -- mass missing")

plt.figure("1")
x = np.arange(0, b, 0.01)
plt.hist(lams, bins=1000, density=True)
if c <= 1:
    lmax = max(mc(x))
else:
    range_x = np.arange(a, b, 0.1)
    lmax = max(mc(range_x))
plt.ylim(0, 1.25 * lmax)
plt.xlim(-500, 12400)
plt.plot(x, mc(x), '-', linewidth=2)
plt.xlabel("Eigenvalues")
plt.ylabel("Density")
plt.title(f"MP-Spike-Model (Var = {v2}, q = {c}, p = {p}, n = {n})", fontsize=12)
plt.text(0.8, 0.1, f"Spike = {lams[-1]:.5f}", fontsize=8, transform=plt.gca().transAxes)
if c > 1:
    plt.text(a/3, 1.15 * lmax, f"The pole at zero has density {(c - 1)/c:.2f}", fontsize=8)


plt.figure("2")
plt.hist(Leading, bins=20, alpha=0.9, color='green')
plt.hist(beta_Norm, bins=20, alpha=0.8, color="blue")
plt.title('Leading Eigenvector Entries vs. Beta')
plt.xlim(-0.15, 0.15)
plt.xlabel('Entries')
plt.ylabel('Frequency')
stats_text = (
    f"Leading Entries-Green\n"
    f"Mean: {mean_L:.8f}\n"
    f"Std Dev: {std_dev_L:.8f}\n"
    f"Skewness: {skewness_L:.4f}\n"
    f"Kurtosis: {kurt_L:.4f}"
)
stats_text_2 = (
    f"Beta/|Beta|-Blue\n"
    f"Mean: {np.mean(beta_Norm):.8f}\n"
    f"Std Dev: {np.std(beta_Norm):.8f}\n"
    f"Skewness: {skew(beta_Norm.flatten()):.4f}\n"
    f"Kurtosis: {kurtosis(beta_Norm.flatten()):.4f}"
)
plt.gca().text(0.65, 0.95, stats_text, transform=plt.gca().transAxes, fontsize=10,
               verticalalignment='top', bbox=dict(boxstyle="round", facecolor="white", alpha=0.5))
plt.gca().text(0.03, 0.95, stats_text_2, transform=plt.gca().transAxes, fontsize=10,
               verticalalignment='top', bbox=dict(boxstyle="round", facecolor="white", alpha=0.5))
plt.show()
