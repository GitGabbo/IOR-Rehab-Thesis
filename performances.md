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

| Exercise | Accuracy Mean                          | Accuracy Max                           | Accuracy Min                           | Time Mean (s) | Time Max (s)   | Time Min (s)  |
| -------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | ------------- | -------------- | ------------- |
| 1        | 0.9737                                 | 0.9677                                 | <span style="color:#f77">0.9799</span> | 24483 (6.80h) | 54939 (15.26h) | 8993 (2.50h)  |
| 2        | 0.9864                                 | <span style="color:#f77">0.9881</span> | 0.9847                                 | 22527 (6.26h) | 46028 (12.79h) | 7053 (1.96h)  |
| 3        | <span style="color:#f77">0.9928</span> | 0.9880                                 | 0.9904                                 | 19791 (5.50h) | 40657 (11.29h) | 10381 (2.88h) |
| 4        | 0.9917                                 | <span style="color:#f77">0.9942</span> | <span style="color:#f77">0.9942</span> | 19141 (5.32h) | 33295 (9.25h)  | 9497 (2.64h)  |
| 5        | <span style="color:#f77">0.9907</span> | 0.9889                                 | 0.9898                                 | 31027 (8.62h) | 63427 (17.62h) | 9480 (2.63h)  |

## 2. Multimodal NN Performances

| Exercise | Avg Accuracy Mean                      | Avg Accuracy Max                       | Avg Accuracy Min | Time Mean (s) | Time Max (s)  | Time min (s)  |
| -------- | -------------------------------------- | -------------------------------------- | ---------------- | ------------- | ------------- | ------------- |
| 1        | 0.9914                                 | <span style="color:#f77">0.9922</span> | 0.9914           | 3170 (52.83m) | 3100 (51.67m) | 2916 (48.60m) |
| 2        | <span style="color:#f77">0.9858</span> | 0.9848                                 | 0.9849           | 3027 (50.45m) | 2975 (49.58m) | 2605 (43.42m) |
| 3        | <span style="color:#f77">0.9904</span> | 0.9888                                 | 0.9800           | 4208 (70.13m) | 3897 (64.95m) | 4075 (67.92m) |
| 4        | 0.9892                                 | <span style="color:#f77">0.9918</span> | 0.9902           | 2880 (48.00m) | 2973 (49.55m) | 2829 (47.15m) |
| 5        | <span style="color:#f77">0.9898</span> | 0.9880                                 | 0.9890           | 2639 (43.98m) | 3218 (53.63m) | 2918 (48.63m) |

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
