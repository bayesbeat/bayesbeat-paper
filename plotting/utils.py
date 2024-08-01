"""Plotting utilities"""

import matplotlib.pyplot as plt
import numpy as np


def compute_residuals(y_data, y_fit, sigma_constant_noise, sigma_amp_noise):
    return (y_data - y_fit) / np.sqrt(
        (y_fit * sigma_amp_noise) ** 2 + sigma_constant_noise**2
    )


def get_duration(filename: str, index: int) -> float:
    import hdf5storage

    try:
        data = hdf5storage.loadmat(filename)
    except ValueError:
        data = read_hdf5_to_dict(filename)
    times = data["ring_times"].T[index]
    valid_times = np.isnan(times)
    return times[~valid_times][-1]


def get_frequency(filename: str, index: int) -> float:
    import hdf5storage

    try:
        data = hdf5storage.loadmat(filename)
    except ValueError:
        data = read_hdf5_to_dict(filename)
    freq = data["freq"][index]
    return float(freq)


def add_log10_bayes_factor_colorbar(mappable, ax):
    cbar = plt.colorbar(mappable, label=r"$\log_{10} \cal{B}$", ax=ax)
    cbar.set_ticks(cbar.get_ticks())
    cbar_tick_labels = [
        r"$" + ("-" if str(t)[0] == "-" else "") + r"10^{" + str(int(np.abs(t))) + r"}$" for t in cbar.get_ticks()
    ]
    cbar_tick_labels[2] = "0"
    cbar.set_ticklabels(cbar_tick_labels)


def get_bayes_factor_markers(vals, threshold=10):
    markers = []
    for v in vals:
        if v > threshold:
            markers.append("^")
        elif v < -threshold:
            markers.append("v")
        else:
            markers.append("o")
    return markers
