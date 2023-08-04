# Performances

For all the following tables:

- Accuracy Mean: it refers to the accuracy of the model trained by adjusting the frame number to the mean number of frames of all videos of that excercise
- Accuracy Max: it refers to the accuracy of the model trained by adjusting the frame number to the maximum number of frames of all videos of that excercise
- Accuracy Min: it refers to the accuracy of the model trained by adjusting the frame number to the minimum number of frames of all videos of that excercise
- Time Mean: it refers to elapsed time for training and validating the model with the leave-one-out cross validation by adjusting the frame number to the mean number of frames of all videos of that excercise
- Time Min: it refers to elapsed time for training and validating the model with the leave-one-out cross validation by adjusting the frame number to the min number of frames of all videos of that excercise
- Time Max: it refers to elapsed time for training and validating the model with the leave-one-out cross validation by adjusting the frame number to the max number of frames of all videos of that excercise

| Exercise | Mean frame number | Max Frame Number | Min Frame Number |
| -------- | ----------------- | ---------------- | ---------------- |
| 1        | 164               | 380              | 53               |
| 2        | 145               | 319              | 40               |
| 3        | 102               | 219              | 30               |
| 4        | 122               | 223              | 55               |
| 5        | 270               | 584              | 68               |

## 1. TimeSeries NN Performances

| Exercise | Accuracy Mean                          | Accuracy Max | Accuracy Min | Time Mean (s) | Time Max (s) | Time Min (s) |
| -------- | -------------------------------------- | ------------ | ------------ | ------------- | ------------ | ------------ |
| 1        |                                        |              |              |               |              |              |
| 2        |                                        |              |              |               |              |              |
| 3        | <span style="color:#f77">0.9928</span> | 0.9880       | 0.9904       | 19791         | 40657        | 10381        |
| 4        |                                        |              |              |               |              |              |
| 5        |                                        |              |              |               |              |              |

<details>
    <summary>Old wrong times (keeping them just in case)</summary>

## WRONG TimeSeries NN Performances

| Exercise | Accuracy Mean                            | Accuracy Max                             | Accuracy Min                             | Time Mean (s) | Time Max (s) | Time Min (s) |
| -------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ------------- | ------------ | ------------ |
| 1        | 0.978166                                 | <span style="color:#f77">0.981659</span> | 0.973799                                 | 153           | 375          | 58           |
| 2        | 0.955085                                 | <span style="color:#f77">0.961017</span> | 0.953390                                 | 147           | 303          | 38           |
| 3        | <span style="color:#f77">0.968000</span> | 0.967200                                 | 0.956800                                 | 97            | 216          | 34           |
| 4        | 0.965975                                 | 0.964315                                 | <span style="color:#f77">0.967635</span> | 116           | 212          | 55           |
| 5        | 0.978704                                 | 0.980556                                 | <span style="color:#f77">0.981481</span> | 205           | 478          | 63           |

</details>

<details>
    <summary>Old perf</summary>

1. Videos Neural Network separeted performances

| Exercise | Target   | Accuracy Mean | Accuracy Max | Accuracy Min |
| -------- | -------- | ------------- | ------------ | ------------ |
| 1        | Goal     | 0.931709      | 0.921397     | 0.960699     |
| 1        | Width    |               |              |              |
| 1        | Head     |               |              |              |
| 1        | Shoulder |               |              |              |
| 1        | Trunk    |               |              |              |
| 2        | Goal     | 0.915254      | 0.911017     | 0.919492     |
| 2        | Width    | 0.889831      | 0.906780     | 0.923729     |
| 2        | Head     | 0.915254      | 0.911017     | 0.923729     |
| 2        | Shoulder | 0.881356      | 0.885593     | 0.906780     |
| 2        | Trunk    | 0.932203      | 0.936491     | 0.944915     |
| 3        | Goal     | 0.924000      | 0.920000     | 0.920000     |
| 3        | Width    | 0.912000      | 0.916000     | 0.912000     |
| 3        | Head     | 0.976000      | 0.980000     | 0.980000     |
| 3        | Shoulder | 0.976000      | 0.972000     | 0.976000     |
| 3        | Trunk    | 0.944000      | 0.944000     | 0.948000     |
| 4        | Goal     |               |              |              |
| 4        | Width    |               |              |              |
| 4        | Head     |               |              |              |
| 4        | Shoulder |               |              |              |
| 4        | Trunk    |               |              |              |
| 5        | Goal     |               |              |              |
| 5        | Width    | 0.925926      |              |              |
| 5        | Head     |               |              |              |
| 5        | Shoulder |               |              |              |
| 5        | Trunk    |               |              |              |

</details>

## 2. Multimodal NN Performances

| Exercise | Avg Accuracy Mean                      | Avg Accuracy Max                       | Avg Accuracy Min | Time Mean (s) | Time Max(s) | Time min (s) |
| -------- | -------------------------------------- | -------------------------------------- | ---------------- | ------------- | ----------- | ------------ |
| 1        | 0.9914                                 | <span style="color:#f77">0.9922</span> | 0.9914           | 3170          | 3100        | 2916         |
| 2        | <span style="color:#f77">0.9858</span> | 0.9848                                 | 0.9849           | 3027          | 2975        | 2605         |
| 3        | <span style="color:#f77">0.9904</span> | 0.9888                                 | 0.9800           | 4208          | 3897        | 4075         |
| 4        | 0.9892                                 | <span style="color:#f77">0.9918</span> | 0.9902           | 2880          | 2973        | 2829         |
| 5        | <span style="color:#f77">0.9898</span> | 0.9880                                 | 0.9890           | 2639          | 3218        | 2918         |

<details>
    <summary>All performances metrics</summary>

| Exercise | Target   | Accuracy Mean | Accuracy Max | Accuracy Min | Time Mean (s) | Time Max (s) | Time min (s) |
| -------- | -------- | ------------- | ------------ | ------------ | ------------- | ------------ | ------------ |
| 1        | Goal     | 0.996         | 0.996        | 0.996        | 465           | 441          | 453          |
| 1        | Width    | 0.987         | 0.987        | 0.987        | 641           | 644          | 693          |
| 1        | Head     | 0.996         | 1.000        | 0.996        | 992           | 1112         | 810          |
| 1        | Shoulder | 0.987         | 0.987        | 0.987        | 626           | 452          | 443          |
| 1        | Trunk    | 0.991         | 0.991        | 0.991        | 446           | 451          | 517          |
|          |          |               |              |              |               |              |              |
| 2        | Goal     | 0.996         | 0.996        | 0.996        | 817           | 798          | 780          |
| 2        | Width    | 0.966         | 0.966        | 0.970        | 858           | 855          | 519          |
| 2        | Head     | 0.996         | 0.996        | 0.996        | 464           | 441          | 424          |
| 2        | Shoulder | 0.975         | 0.970        | 0.966        | 456           | 440          | 432          |
| 2        | Trunk    | 0.996         | 0.996        | 0.996        | 432           | 441          | 450          |
|          |          |               |              |              |               |              |              |
| 3        | Goal     | 0.996         | 0.996        | 0.984        | 677           | 633          | 880          |
| 3        | Width    | 0.976         | 0.976        | 0.976        | 864           | 819          | 882          |
| 3        | Head     | 1.000         | 0.996        | 1.000        | 910           | 672          | 709          |
| 3        | Shoulder | 0.992         | 0.988        | 0.992        | 709           | 953          | 724          |
| 3        | Trunk    | 0.988         | 0.988        | 0.988        | 1048          | 820          | 880          |
|          |          |               |              |              |               |              |              |
| 4        | Goal     | 0.996         | 0.996        | 0.992        | 606           | 554          | 616          |
| 4        | Width    | 0.979         | 0.983        | 0.979        | 575           | 578          | 544          |
| 4        | Head     | 0.988         | 0.988        | 0.988        | 565           | 531          | 544          |
| 4        | Shoulder | 0.996         | 0.996        | 0.996        | 568           | 607          | 545          |
| 4        | Trunk    | 0.987         | 0.996        | 0.996        | 566           | 703          | 580          |
|          |          |               |              |              |               |              |              |
| 5        | Goal     | 0.995         | 0.986        | 0.986        | 390           | 636          | 623          |
| 5        | Width    | 0.991         | 0.991        | 0.991        | 617           | 479          | 471          |
| 5        | Head     | 0.963         | 0.963        | 0.968        | 473           | 481          | 473          |
| 5        | Shoulder | 1.000         | 1.000        | 1.000        | 514           | 760          | 776          |
| 5        | Trunk    | 1.000         | 1.000        | 1.000        | 645           | 772          | 575          |

</details>
