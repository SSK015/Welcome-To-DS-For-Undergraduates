## Click here [Slide(pdf)](https://web.stanford.edu/class/cs246/slides/06-dim_red.pdf))
## What is the task of Dim-red?: 
find latent factors, discover the axes of data.
### evaluate dimension by the value of rank

# SVD(Singular Value Decomposition)
### What is Singular Value?
#### Definition of SV in Mathematics
The square roots.
See [SV(wiki)](https://en.wikipedia.org/wiki/Singular_value#Basic_properties)

## Important formula
$\mathbf{A}$ ~ $\mathbf{U} $ * $\sum $ * $\mathbf{V}^\mathrm{T}$
A : Input data (m documents * n terms)
U : Left Singular vectors (m documnets * r concepts)
V : Right Singular vectors (n * r)
$\sum $ : Singular values
<!-->$\displaystyle \sum<!-->
### understand the picture given in the slide to promote comprehension.
### some properties in the above formula:
#### U, $\sum $, V : unique matrix;
#### U, V: column orthonormal
#### $\sum $ :diagonal

### What is concept? 
Given in the examples, it can be features ans categories of different data.

### Structure 
example : 
- A 7 x 5 ; 
- U 7 x 3 ;
- $\sum $ 3 x 3;
- V : 3 x 5 .

### Algorithm
See the slides. We may offer other materials.

 