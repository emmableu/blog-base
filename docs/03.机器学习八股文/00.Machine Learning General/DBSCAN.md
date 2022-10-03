---
title: DBSCAN
date: 2022-10-02 22:29:13
permalink: /pages/569419/
categories:
  - 机器学习八股文
  - Machine Learning General
tags:
  - 
---



## The concepts of DBScan

Before we start looking at these concepts, we must generate an imaginary dataset first. Here it is. Suppose that we are dealing with a two-dimensional feature space where our samples can be expressed as points (i.e. as (x_1, x_2) coordinates). It could then look like this:  

![](https://raw.githubusercontent.com/emmableu/image/master/202210022231818.png)

When performing DBSCAN, two parameters must be provided before the algorithm is run. The first is the **epsilon value**, or $\epsilon$. This value indicates some distance around a point, which can be visualized as a circle with a diamater of $\epsilon$ around a point. Note that each point has the same $\epsilon$, but that we draw the circle for just one point below.

The second is the **minimum number of samples**. This number indicates the minimum number of samples (including the point itself) that should be within the epsilon range (i.e., the circle) for a point to be considered a _core point_. We will now look at what these are.

![](https://raw.githubusercontent.com/emmableu/image/master/202210022232489.png)



### Core Points

Suppose that we have some epsilon $\epsilon$ and set the minimum number of points to 3. We will now look at two points of the dataset. On the left, we look at the above point, while on the right, we look at one of the middle points.

> A point _p_ is a _core point_ if at least minPts points are within distance _ε_ of it (including _p_).


In other words, in our example, a point is a core point if at least 3 points, including itself, are within the circle. As becomes clear, both points that we are looking at are so-called core points.

The great thing of core points is that they are likely part of a cluster, because they are in the vicinity of other points. That's why they are so important in the DBSCAN algorithm.

![](https://raw.githubusercontent.com/emmableu/image/master/202210022234240.png)

If the dataset were larger (e.g. because we zoomed into a particular area), and another point would be inspected, we could arrive at the conclusion that it is not a core point. The example below illustrates why: there are only two points, including itself, in the $\epsilon$ based vicinity of the point. Since minPoints = 3 and 
2 < 3, this is not a core point.

![](https://raw.githubusercontent.com/emmableu/image/master/202210022236462.png)

### Directly Reachable Points

If a point is not a core point, we must look whether it is **directly reachable**.

> A point _q_ is _directly reachable_ from _p_ if point _q_ is within distance _ε_ from core point _p_. Points are only said to be directly reachable from core points.


In the example above, we saw that the extra point we were looking at is not a core point. But is it directly reachable?

It seems to be the case:

- The closest point to the point we were looking at is a core point, since its $\epsilon$ circle contains 4 points, which exceeds the minimum of 3.
- The point itself lies within the $\epsilon$ circle for the closest core point.

This means that it is directly reachable.

![](https://raw.githubusercontent.com/emmableu/image/master/202210022237204.png)



### Reachable Points

Another concept in DBSCAN is the one of **reachable points:**

Points are reachable from some point if we can draw a path to it, through points directly reachable from the points on the path (i.e. core points on the path), to the specific point. In our example, B is reachable from A, and we display just one of the paths through which B can be reached.

![](https://raw.githubusercontent.com/emmableu/image/master/202210022239957.png)


### Outliers

If a point is not reachable from any other point, it is called an outlier:

> All points not reachable from any other point are _outliers_ or _noise points_.

In other words, if we cannot draw a path from a core point to another point (i.e. if it's not directly reachable nor reachable from the particular point), it's considered an outlier. This is what makes DBSCAN so good for clustering with outlier detection: it can signal outliers natively.

![](https://raw.githubusercontent.com/emmableu/image/master/202210022240273.png)

## How everything fits together: DBScan in pseudocode

Now that we know about all the DBSCAN concepts, i.e. the _what_, we can now dive into the _how_. In other words, it's time to look at how DBSCAN works. Funnily, despite the complex name, the algorithm is really simple (Wikipedia, 2007):

1. We set values for $\epsilon$ and `minPoints`.
2. We randomly select a point from the samples that has not been checked before.
3. We retrieve the `neighborhood` for this point. If it equals or exceeds `minPoints`, we signal it as a cluster. Otherwise, we label it as noise.
4. We signal the $\epsilon$-neighborhood as being part of the cluster. This means that for each point of that neighborhood, its own  $\epsilon$-neighborhood is added to the cluster as well, and so on, and so on. We continue until no further point can be added to the cluster
5. We now start at (2) again, unless all points have been checked and labeled.

