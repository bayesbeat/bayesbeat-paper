"""Plotting utilities"""

import matplotlib.pyplot as plt
import numpy as np
from bayesbeat.utils import read_hdf5_to_dict


model_colours = {
    "model_1_constant_noise": "C0",
    "model_1": "C1",
    "model_3": "C2",
}

model_labels = {
    "model_1_constant_noise": r"$M_1, \xi_\text{A}=0$",
    "model_1": r"$M_1, \xi_\text{A} > 0$",
    "model_3": r"$M_3, \xi_\text{A} > 0, T=7$",
}


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


def plot_fit(
    x_data,
    y_data,
    y_fit,
    sigma_constant_noise: float = None,
    sigma_amp_noise: float = None,
    ln_evidence: float = None,
    colour="C0",
    label=None,
):
    figsize = plt.rcParams["figure.figsize"].copy()
    figsize[0] = 1.8 * figsize[0]
    figsize[1] = 1.6 * figsize[1]
    fig, axs = plt.subplot_mosaic(
        [["fit", "fit", "fit", "empty"], ["fit", "fit", "fit", "empty"], ["res", "res", "res", "dist"]],
        figsize=figsize,
    )

    axs["fit"].scatter(x_data, y_data, color="k", s=1, label="Data")
    axs["fit"].plot(x_data, y_fit, c=colour, label="Fit")
    axs["fit"].set_yscale("log")
    axs["fit"].legend()

    residuals = compute_residuals(
        y_data,
        y_fit,
        sigma_constant_noise=sigma_constant_noise,
        sigma_amp_noise=sigma_amp_noise,
    )

    axs["res"].scatter(x_data, residuals, s=1, c=colour, lw=0.0)

    axs["dist"].hist(residuals, 32, histtype="step", orientation="horizontal", color=colour)

    axs["empty"].axis("off")
    # axs["dist"].legend()
    # axs["fit"].grid()
    axs["res"].set_xlabel("Time [s]")
    axs["fit"].set_ylabel("$d$")
    # axs["res"].grid()
    axs["res"].set_ylabel(r"$\mathcal{R}$")
    axs["res"].sharex(axs["fit"])
    axs["res"].sharey(axs["dist"])
    axs["fit"].tick_params(labelbottom=False)
    axs["dist"].tick_params(labelleft=False)
    axs["dist"].set_xlabel("Counts")
    # axs["dist"].grid()
    # axs["res"].set_xscale("log")

    if label is not None:
        axs["empty"].text(0., 0.66, label, fontsize=8)
    if ln_evidence is not None:
        axs["empty"].text(0., 0.56, r"$\log_{10} Z = " + f"{ln_evidence / np.log(10):.1f}" + r"$", fontsize=8)

    plt.tight_layout()
    return fig
