<!-- 
.. title: Ranking NCAA Basketball Teams with PageRank
.. slug: ncaab-pagerank
.. date: 2014-11-13
.. tags: sports
.. author: Ryan Ranson
-->

I was recently trying to think of good ways to rank college basketball teams and thought I had a unique idea in applying Google's PageRank algorithm to the problem. It turns out I am not as original as I had hoped and this approach seems to be fairly widely used. The most useful example I found was [applied to NFL teams](http://http://www.ncsu.edu/crsc/reports/ftp/pdf/crsc-tr06-19.pdf) but it generalizes easily to any other sport. I was hoping to find up-to-date or historical rankings for NCAA basketball using this method but was unable to find anything publicly available. I'll attempt to construct these rankings for the 2013 season and compare it to the results of other popular methods. If the results are useful, I hope to maintain weekly rankings for the current season.

I obtained the full 2013-2014 season of NCAA men's basketball game scores from [Spreadsheet Sports](https://www.spreadsheet-sports.com/2014-ncaa-mens-basketball-game-results-data/). Let's begin with data loading and preparation:

```r
library(RCurl)
library(devtools)

games.url <- getURL("https://raw.githubusercontent.com/ransonr/SportsAnalytics/master/data/NCAAM_2014_FullSeason.csv")
games <- read.csv(text = games.url, header = TRUE, stringsAsFactors = FALSE)
games <- games[games$Team.Differential > 0,] # Data is duplicated for home/away
games$Date <- as.Date(games$Date, "%m/%d/%Y")

teams <- unique(c(games$Team, games$Opponent))
n <- length(teams)
```

We now need to create the n x n hyperlink matrix H, where entry (i,j) corresponds to the total number of points team j outscored team i by. This can be thought of as team i's "vote" given to team j.

```r
# Entry (i, j) of H will be the total # of points team j outscored team i by
H <- matrix(0, nrow = n, ncol = n)
colnames(H) <- teams
rownames(H) <- teams

for (i in 1:nrow(games)) {
  t1 <- games$Team[i]
  t2 <- games$Opponent[i]
  H[c(t2), c(t1)] <- H[c(t2), c(t1)] + games$Team.Differential[i]
}
```

Next we need to adjust the matrix H to be stochastic. To make it stochastic we need to ensure all entries are nonnegative (done) and all rows sum to 1. To make each row sum to 1 we simply divide each entry by it's row sum. We might run into an issue if a team has an undefeated season, in which case their row will contain all 0's. In this case, we can simply plug 1/n into each entry of the row: 

```r
# Divide rows by row sums
H <- H / rowSums(H)

# If a team is undefeated, the whole row will be zero -> just put 1/n in each entry
for (i in 1:nrow(H)) {
  if (sum(H[i,]) == 0) {
    H[i,] <- 1 / n
  }
}
```

I implemented the PageRank algorithm using the [power method](http://en.wikipedia.org/wiki/PageRank#Power_Method) and the source can be viewed [here](https://github.com/ransonr/SportsAnalytics/blob/master/R/PageRank.R).

```r
source_url("https://raw.githubusercontent.com/ransonr/SportsAnalytics/master/R/PageRank.R")

page.rank <- PageRank(H, 0.85)

rank.df <- data.frame(PageRank = page.rank$pr)
rank.df$Rank <- rank(-page.rank$pr)
rank.df <- rank.df[with(rank.df, order(Rank)),]
```

So how do the results look?

```r
head(rank.df, 25)
```

```text
##                PageRank Rank
## Louisville     0.014946    1
## Arizona        0.012374    2
## Duke           0.012279    3
## Louisiana Tech 0.012043    4
## Wichita St     0.011447    5
## Florida        0.011392    6
## Kansas         0.010888    7
## San Diego St   0.010846    8
## Virginia       0.010807    9
## SF Austin      0.010564   10
## Cincinnati     0.010465   11
## UCLA           0.010114   12
## Kentucky       0.009912   13
## N Dakota St    0.009901   14
## New Mexico     0.009664   15
## Harvard        0.009640   16
## Connecticut    0.009593   17
## Iowa           0.009389   18
## Gonzaga        0.009387   19
## Wisconsin      0.009233   20
## Oklahoma St    0.009187   21
## WI Green Bay   0.009123   22
## Southern Miss  0.009105   23
## Tennessee      0.009092   24
## Michigan St    0.008921   25
```

This looks halfway promising! Plenty of familiar names in the top 25 here although Louisana Tech jumps out as the first and most obvious aberration. In a later post I intend to compare the results from this ranking method to the results of other popular ranking methods (RPI, Ken Pom, etc...).
