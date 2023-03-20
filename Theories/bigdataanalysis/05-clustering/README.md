### Click here [Slide(pdf)](https://web.stanford.edu/class/cs246/slides/05-clustering.pdf)

### What is Clustering?
That is to say, given a set of **points**, We can define **a concept of distance** between these points. Then, we group the points into **some number of clusters**, which is known as "簇" in Chinese.  

#### distance : mainly Euclidean or Jaccard

### Why is Clustering hard?
- #### Too many dimensions: isolated points

### Two main methods: 
- ##### Hierarchical: bottom up and top down
- ##### Assign: assign points to a Existing cluster

## Hierarchical(between clusters): 
#### note:
1. represent a cluster.
2. determine the nearness of clusters.
3. when to stop merging clusters.
#### Euclidean case:
1. centroid(average)
2. (1) distance of centroids
   (2) shortest distance between two clusters

#### UnEuclidean case:
1. centroid(a point(existing) "closet" to others)
- maxium/average/square of dis  
2. various distance and cohesion measures



