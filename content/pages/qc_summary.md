Title: Summary of quantum computing work
no_aside: True
load_mathjax: True

Read on for some background,
or [jump ahead](#qc-my-work) to the discussion of my contributions.

### Background

The discovery of Shor's factoring algorithm (along with schemes for
quantum error correction) led to an explosion of research in quantum
computing in the last 25 years. The subtlety of designing quantum algorithms
to achieve meaningful speedup attracted many theoreticians;
the application to public-key codebreaking attracted many funding agencies.
Another important factor was that qubits, the fundamental
building block of quantum computers, are just quantum systems with two
accessible energy levels.

These turn out to be ubiquitous, and so a huge array of experimental
fields were each able to put forth their own proposals for how to
realize qubits. Experimentally, quantum computing is a profound
engineering challenge. To make the magic work, you need to keep your
system coherent, which requires decoupling it from the rest of the
world.  However, to use your computer to do anything, the qubits need
to be able to communicate with each other and the
experimenter... which requires coupling it to the rest of the
world. Balancing the tradeoff between these two concerns is the
fundamental issue in experimental quantum computing.

Superconducting qubits -- the area I studied -- are a popular choice.
The fabrication technologies used in building them are largely the same
as in semiconductors, and interconnections consist of patterned
electrical circuits. Superconductivity provides a low loss electrical
environment; since dissipation unavoidably leads to decoherence, this is
essential for a qubit. Even so, superconducting qubits typically suffer from
worse coherence times relative to other technologies. Researchers proposed
several different styles of superconducting qubit. All of them were based
on Josephson junctions, usually based on a thin insulating layer between
two superconductors. These provided the necessary nonlinearity to the
system to restrict it to two energy levels.

I worked in a group at the University of Maryland (led by Fred Wellstood,
Chris Lobb, and Bob Anderson) that studied dc SQUID phase qubits. Unpacking
that, dc SQUID indicates that it was a ring with two Josephson junctions,
in contrast to a single junction phase qubit. This design, originally
proposed by [Martinis et al.](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.89.117901),
conceived of one junction as the qubit junction and the other as a filter. By
using a junction in the filter, enough degrees of freedom were maintained
to bias the system to appropriate operating conditions. In Josephson junctions,
the dc current through the junction corresponds to the phase difference in the
superconducting wavefunction in the two sides of the junction. When you
include the capacitance of the junction, you get an equation of motion for
the phase difference that looks like motion in a "tilted washboard" potential.
By appropriately biasing the dc SQUID with current and flux, you can operate
in a regime where this potential is anharmonic, allowing you to isolate the
two lowest resonances of the well as qubit states.

Readout was handled by
tunneling out of this potential well. When the qubit tunneled, this produced
a measurable voltage pulse because of the change in phase. Tunneling is
exponentially enhanced with increasing energy, giving a method for
differentiating between 0 and 1. Because
of the statistical nature of quantum measurements, the final measurement
was built up from many repeated runs.

<h3 id="qc-my-work">My work</h3>

The readout method I just described was a key weakness of the phase qubit
for at least two reasons. In the "voltage state", the junction dissipates
energy, requiring a relatively lengthy cooling period afterward to return
to base temperature. This led to a ceiling on the experimental repetition
rate of a few hundred per second. This made building up enough counts for
statistically clean measurements slow, reducing turnaround time on the
devices we were characterizing. A more fundamental issue is that tunneling
based readout is not projective: following the tunneling measurement, the
system is generally not in the same state that you just measured. While
this doesn't represent a problem for device characterization, it's a
dealbreaker for general fault tolerant quantum computation. I thought a
good research direction might be to try to resolve this issue.

We took inspiration from the [Josephson bifurcation amplifier](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.93.207002). A Josephson junction
can be viewed as a nonlinear inductance, and oscillators built using this
nonlinearity can exhibit bistable response to rf excitation. By biasing
near the bifurcation where the bistability appeared, small changes in the
frequency arising from modulation of junction parameters could correspond to
large changes in a reflected rf signal. We believed that it would be
possible to use the filter junction of the dc SQUID in a fashion similar to
this. [A theoretical study](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.77.214512) of the dc SQUID phase qubit predicted that when the qubit
junction was excited, it would lead to a shift in circulating current in
the SQUID loop. This would modify the current through the filter junction,
shifting the Josephson inductance enough to enable a rf reflectometry readout
that would be tunneling free and projective.

I started designing circuits to test this readout approach. The major
modification from earlier dc SQUID qubit designs in our lab was the addition
of a large shunt capacitor before the SQUID loop. The capacitor effectively
increased the capacitance of the filter junction, depressing the resonant
frequency of that system. This moved the frequency of the signal used for
readout far from the transition frequency for the qubit to minimize unwanted
transitions during readout. I then fabricated devices for study. The
circuits were patterned on silicon (and later sapphire) wafers using
photolithography, and aluminum deposited using a double-angle thermal
evaporation process. A controlled oxidation step between the two angles of
the evaporation formed the Josephson junctions.

The superconducting transition temperature of aluminum is close to 1 K;
to achieve those temperatures we mounted our device in a [dilution
refrigerator](https://en.wikipedia.org/wiki/Dilution_refrigerator). We
had already installed heavily filtered low frequency lines for qubit
measurement and control, and we installed some new microwave lines (
along with a cryogenic microwave circulator for isolation) for the
reflectometry measurement.

When we measured the first sample, we found that the microwave setup
(including the on-chip lumped element microwave resonator we were measuring)
looked good, but we didn't succeed in measuring the qubit this way.
However, while characterizing the device, we realized that by operating
with rf power slightly below the bifurcation regime, we could use the
resonator as a sensitive probe to measure 1/f flux noise in the device.
This type of noise is [ubiquitous in solid state systems](
https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.53.497) and
is an important source of decoherence in many superconducting qubit designs.
We found values for our system consistent with [older results](
https://aip.scitation.org/doi/10.1063/1.98041) showing weak dependence on
most circuit parameters.

After testing a few more devices and ruling out various aspects of the
experimental setup as explanations of why the measurement failed, I
became suspicious about how well the theory of the projective
microwave measurement was fitting our qubits.  When I reexamined the
theory, a central approximation was that the two junctions of the dc
SQUID were well isolated by the large inductance of the SQUID
loop. Early phase qubit designs used relatively large area Josephson
junctions. One reason for this was to reduce the importance of
critical current fluctuations. However, other researchers showed that
[two-level
systems](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.95.210503)
in the Josephson junction dielectric played a more important role. The
natural way to minimize these is to use smaller junctions. As junctions
grow smaller, the inductance of the Josephson junction itself grows. In
moving to smaller junctions, we now had Josephson inductances in the
filter arm that were non-trivial compared to the combined inductance of the
SQUID loop and qubit junction.

The original theory viewed the dynamics as a nonlinear perturbation to
two harmonic oscillators given by each junction. My revised theory instead
considered a basis where the appropriate harmonic oscillators are the two
normal modes of the circuit. With appropriate parameters, this normal modes
approach returned to the independent junction model. After working out the
new theory, we found it was substantially better at explaining the behavior
of other devices being studied in the lab.

I spent a while longer working on new designs with stronger nonlinearities
and more tunability, with the goal of demonstrating microwave readout in
our systems. Eventually, I switched over to the main research direction of
our group: trying to understand and improve the qubit lifetime $T_1$ in our
systems. With Rangga Budoyo, another graduate student in the lab, I
designed and built a new qubit. This device used a large interdigitated
capacitor on the smaller junction to improve dielectric quality factor,
and handled microwave excitation of the qubit using a coplanar waveguide
modeled to have more controlled coupling to the qubit.

As we characterized the new qubit, we found it showed unusual spectroscopic
features. In particular, the peak shape was highly broadened on one side.
We found that we could explain this well as a consequence of the large
shunt capacitor in front of the SQUID. I showed that when the capacitor was
included in my quantum circuit theory, you could extract an effective
[Jaynes-Cummings model](https://en.wikipedia.org/wiki/Jaynes%E2%80%93Cummings_model) for the system. This model, which had become central
in superconducting quantum computing, describes the coupling between a
two-level system (e.g. a qubit) and a harmonic oscillator (e.g. a microwave
cavity.) In the dispersive limit of the model, the frequency of the qubit
is shifted proportional to the number of excitations in the cavity. Since
we had chosen a large capacitance (and thus low frequency filter) to
maximize isolation to the bias leads, thermal excitation of the filter modes
was likely substantial. This led to many relatively narrow individual peaks
being superposed to give the broadened measured peak.