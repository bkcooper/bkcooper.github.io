Title: Brief research synopses
Slug: research
aside_title: Research
toc_list: photophysics, quantumcomp
toc_text: Computational microscopy, Quantum computing

<h2 id='photophysics'>Photophysics and inference from images</h2>

Fluorescence microscopy has become an essential tool for biological
research, allowing scientists to visualize subcellular processes
(often in living cells) with protein specificity and impressive
spatial and temporal precision.  Despite this power, microscopic
images are still imperfect representations of the positions of the
light emitting fluorophores in the sample. Optical diffraction and
unavoidable statistical fluctuations in the measured signal lead to
blurring and noise, even if other error sources are eliminated by
careful measurement. Using optical and computational techniques to
bring images closer to the underlying distribution of fluorophores has
been an active research area for decades. __In [Andrew York's lab](
https://andrewgyork.github.io/) at [Calico](
https://www.calicolabs.com), we have developed approaches to augment
classic deconvolution techniques with extra information about the
photophysical behavior of the emitters.__ For background, read on,
or [jump ahead](#micro-my-work) to the discussion of my contributions.

### Background

The starting point for this approach was [Richardson-Lucy deconvolution](
https://en.wikipedia.org/wiki/Richardson%E2%80%93Lucy_deconvolution),
a deblurring technique invented almost fifty years ago. The algorithm is
mechanically very simple. Each iteration is a multiplicative update of
the previous guess, where the update depends on the ratio between the
measured image and the expected image generated by the current guess:

```python
# H is a linear operator mapping estimates to images
# H_T is the transverse of H (and thus maps images to estimates)

def richardson_lucy(img, guess=None, n_iter=64):
    if guess is None:
        guess = np.ones_like(H_T(img))
    normalizer = H_T(np.ones_like(img))
    for _ in range(n_iter):
        guess *= H_T(img / H(guess)) / normalizer
    return guess
```

Originally, H was just convolution with some point spread function.
However, the algorithm works just as well for any linear operation H.
[Ingaramo et al.](
https://onlinelibrary.wiley.com/doi/abs/10.1002/cphc.201300831) point
out that this makes Richardson-Lucy very flexible and suited for a broad
range of computational microscopy tasks. In particular, it works nicely with
techniques that combine multiple images (which could come from multiple
viewing angles, or different illumination conditions) to arrive at a
final estimate of the object.

Inverse problems like the type Richardson-Lucy solves are usually ill
posed -- the loss of information in mapping from object to image
usually results in many solutions consistent with the data.  The
classic solution to this issue is *regularization*, where an
additional penalty function is added to distinguish among
solutions. This is equivalent to imposing a prior on your object
space; the penalty function says that solutions with high intensity
gradients or total variation (to pick some standard examples) are less
probable and need stronger support in the data. Many of the classic
regularization approaches have sensible interpretations and can be made to
work well. However, there often aren't good ways to decide on how to
parameterize them, leaving non-experts who wish to have a tool that just works
stuck trying to choose parameters. The tweakability of these parameters
can also lead (particularly in the biological microscopy community) to
concerns about adjusting them until you "see what you want to see."

We adapted a different approach. Instead of using priors on the structure
of the object, we decided to pursue priors based on the photophysical
behavior of the molecules being imaged. This has nice conceptual advantages
over other approaches (which one could still incorporate, if desired.)
The models mostly depend on measurable parameters, resolving the criticisms
of the previous paragraph. It also offers a possible tie-in to single
molecule localization microscopy, one of the great microscopy ideas of
recent times. An algorithm that moves seamlessly between the sparsely
tagged regime where localization microscopy (and its attendant high resolution)
works and the more typical densely tagged widefield regime would be very
useful.

We believe that combining deconvolution with photophysics is a
natural road to that goal. Another possibility could be a deep learning
approach. There's been an explosion of work applying neural networks to
microscopy image problems. This is also a worthy approach. However, we
feel there are advantages to our approach that make it worth studying.
With neural networks, the reconstructions can depend on both the imaging
system and the sample being measured. Disentangling the contributions of
these and assessing whether your model generalizes to new samples can
be difficult.

<h3 id="micro-my-work">My work</h3>

Richardson-Lucy corresponds to a special form of gradient descent to find the
maximum likelihood estimate assuming that each pixel of the image is
corrupted by Poisson noise. The distinction from usual gradient descent
is that the step size is fixed, but scaled at each point multipicatively by
the current estimate. One very nice thing feature of the multiplicative update
is that (given a feasible estimate and a positive semidefinite blurring
operator H) it automatically preserves a non-negativity constraint on the
estimate. Much of the performance of Richardson-Lucy derives from this
constraint.

Our first project consisted of __incorporating photobleaching into a
deconvolution algorithm.__ Photobleaching is a process where emitting molecules
irreversibly stop glowing. It is generally seen as a nuisance that reduces
measurable signal


<h2 id="quantumcomp">Earlier work -- quantum computing</h2>

### Background

<h3 id="qc-my-work">My work</h3>

[thesis](https://drum.lib.umd.edu/handle/1903/14932)