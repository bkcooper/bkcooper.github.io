Title: Brief research synopses
Slug: research
aside_title: Research
load_mathjax: True

<h2 id='photophysics'>Photophysics and inference from images</h2>

Fluorescence microscopy has become an essential tool for biological
research, allowing scientists to visualize subcellular processes
(often in living cells) with protein specificity and impressive
spatial and temporal precision.  Despite this power, microscopic
images are still imperfect representations of the positions of the
light-emitting fluorophores in the sample. Optical diffraction and
unavoidable statistical fluctuations in the measured signal lead to
blurring and noise, even if other error sources are eliminated by
careful measurement. Using optical and computational techniques to
bring images closer to the underlying distribution of fluorophores has
been an active research area for decades. __In [Andrew York's lab](
https://andrewgyork.github.io/) at [Calico](
https://www.calicolabs.com), I have developed approaches to augment
classic deconvolution techniques with extra information about the
photophysical behavior of the emitters.__ The backbone of most of our
methods is maximum likelihood estimation, but I've also applied other
techniques (e.g. hidden Markov models, neural networks) to understand
our problems.

In one project I incorporated photobleaching (a destructive process
that extinguishes light-emitting fluorophores) as a prior for maximum
likelihood deconvolution. Although we chose this as a first
modification for its simplicity, it proved surprisingly rich. In the
course of testing our algorithm, I posed a natural question: how can
we fairly compare a multi-exposure method with a single exposure one?
Investigating this led me to consider how to take the best image
possible in the presence of photophysical noise. I developed theory to
determine optimal single exposure times, and discovered the surprising
result that this additional noise limits the expected signal-to-noise
improvement from using bleaching resistant fluorophores. This has
implications for nearly all fluorescent imaging methods. I also
developed a nonlinear extension to the well-known Richardson-Lucy
deconvolution algorithm and applied it to FRET microscopy, a
technique where fluorophore-fluorophore interactions are responsible
for key parts of the signal.

A more in-depth discussion of these
projects is available [here]({filename}microscopy_summary.md).

<h2 id="quantumcomp">Quantum computing</h2>

Google's [quantum supremacy](https://ai.googleblog.com/2019/10/quantum-supremacy-using-programmable.html) result is a spectacular example of the progress
made in quantum computing in the last twenty years. That a roughly 50 qubit
device is so noteworthy is itself a spectacular example of the immense
engineering challenge quantum computing represents. Fifteen years ago,
even within the world of superconducting quantum computing -- where the
qubits are built from small superconducting circuits -- there was no
consensus even on how one should build a single qubit. Many
approaches were studied to learn how to build well performing qubits.
__My Ph.D. [thesis](https://drum.lib.umd.edu/handle/1903/14932) was
an experimental and theoretical study of one particular kind of
superconducting qubit: the dc SQUID phase qubit.__

After learning the ropes in the lab by doing measurements on some
existing devices, I designed a new
version of this qubit with a large shunt capacitor before the circuit.
We expected this to allow projective microwave readout of
the qubit state, in analogy to experiments in other labs. To test this
I built several
versions, using both e-beam and photolithographic techniques, and performed
electronic and microwave measurements on these devices at temperatures
near 50 millikelvin. When the new
readout approach failed, I reviewed the theory we were using and found it
used a key approximation that was no longer appropriate for those device
parameters. I developed new theory to explain the quantum
dynamics of our circuit. This theory became an important tool for our
lab in designing the next generation of qubits to aim for lower loss.
When we built and measured one of these to check the performance, we found
unusual features that seemed explicable by quantum behavior in the shunt
capacitor, in accordance with my theory.

A longer account of this work is available [here]({filename}qc_summary.md).

<h2>Smaller projects</h2>

Before my dissertation, I did some theoretical condensed matter
research.  My undergraduate thesis under [Daniel
Aalberts](http:\\panic.williams.edu) studied a model for the
conjugated polymer family polyacetylene, a starting point for
understanding the fast photoisomerization of light detecting molecules
in the eye. I modified in-house C code to include steric effects in
the model, looked at soliton behavior in odd-length chains, and
studied how mechanically stretching these molecules changed the
transition frequency. Working with [Victor
Yakovenko](http://physics.umd.edu/~yakovenk/), I studied quasi-1D
[organic superconductors](
https://en.wikipedia.org/wiki/Organic_superconductor). We published a
paper discussing the Aharanov-Bohm effect as a unifying theme
explaining the angular magnetoresistance oscillations observed in
these materials.

After my Ph.D., I did a brief postdoc in Ian Appelbaum's lab. I
implemented a proof-of-principle experiment to demonstrate the
feasibility of a capacitive, nonlinear scheme for detecting bound
Majorana fermion excitations in nanowire systems. Instead of
nanowires, I fabricated superconducting-insulating-normal junctions as
a test system to validate the measurement technique. I built a custom
low-capacitance probe to use with a commercial low temperature
measurement system, and performed conductivity measurements
demonstrating the suitability of this approach.