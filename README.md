# Grunch

People are often hesitant to make a decision for the whole group, especially
analytically-minded programmers who recognize the vast amount of variables
involved in satisfying all individuals.
If you do make a lunchplace proposal, other members of the group might disagree
but keep quiet, or voice their opposition and discourage others from making
proposals that might also be rejected.
However, though each individual may not know how to make *everyone* happy,
each person knows what choices would make him/her *unhappy*. 
By first asking "where should we *not* go" , the problem is no longer a
maximization of group happiness, but a minimization of individual unhappiness.

Grunch is a random rejection-based lunchplace decider based on this concept.
Grunch first asks users for general rejections, such as vegetarian-available
only, or places that are within biking distance, then randomly chooses a place
that satisfies the constraints.
If someone doesn't like the randomly chosen place, they can reject it (without
offending Grunch's taste in cuisine), upon which Grunch will remove it from the
available options and randomly choose another place.

