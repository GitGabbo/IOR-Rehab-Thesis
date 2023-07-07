# Performances
For all the following tables:
* Accuracy Mean: it refers to the accuracy of the model trained by adjusting the frame number to the mean number of frames of all videos of that excercise
* Accuracy Max: it refers to the accuracy of the model trained by adjusting the frame number to the maximum number of frames of all videos of that excercise
* Accuracy Min: it refers to the accuracy of the model trained by adjusting the frame number to the minimum number of frames of all videos of that excercise

|Exercise| Mean frame number | Max Frame Number | Min Frame Number |
|--------|-------------------|------------------|------------------|
| 1      | 164               | 380              | 53               |
| 2      | 145               | 319              | 40               |
| 3      | 102               | 219              | 30               |
| 4      | 122               | 223              | 55               |
| 5      | 270               | 584              | 68               |

## 1. TimeSeries NN Performances
|Exercise|Accuracy Mean| Accuracy Max | Accuracy Min | Time Mean (s) | Time Max (s) | Time min (s) |
|--------|-------------|--------------|--------------|-----------|----------|----------|
| 1      | 0.978166    | <span style="color:#f77">0.981659</span>     | 0.973799     | 153 | 375 | 58 |
| 2      | 0.955085    | <span style="color:#f77">0.961017</span>     | 0.953390     | 147 | 303 | 38 |
| 3      | <span style="color:#f77">0.968000</span>    | 0.967200     | 0.956800     | 97 | 216 | 34 |
| 4      | 0.965975    | 0.964315     | <span style="color:#f77">0.967635</span>      | 116 | 212 | 55 |
| 5      | 0.978704    | 0.980556     | <span style="color:#f77">0.981481</span>     | 205 | 478 | 63 |

<details>
    <summary>Old perf</summary>

1. Videos Neural Network separeted performances

|Exercise|  Target  |Accuracy Mean| Accuracy Max | Accuracy Min |
|--------|----------|-------------|--------------|--------------|
| 1      | Goal     | 0.931709    | 0.921397     | 0.960699     |
| 1      | Width    |     |      |      |
| 1      | Head     |     |      |      |
| 1      | Shoulder |     |      |      |
| 1      | Trunk    |     |      |      |
| 2      | Goal     | 0.915254    | 0.911017     | 0.919492     |
| 2      | Width    | 0.889831    | 0.906780     | 0.923729     |
| 2      | Head     | 0.915254    | 0.911017     | 0.923729     |
| 2      | Shoulder | 0.881356    | 0.885593     | 0.906780     |
| 2      | Trunk    | 0.932203    | 0.936491     | 0.944915     |
| 3      | Goal     | 0.924000    | 0.920000     | 0.920000     |
| 3      | Width    | 0.912000    | 0.916000     | 0.912000     |
| 3      | Head     | 0.976000    | 0.980000     | 0.980000     |
| 3      | Shoulder | 0.976000    | 0.972000     | 0.976000     |
| 3      | Trunk    | 0.944000    | 0.944000     | 0.948000     |
| 4      | Goal     |     |      |      |
| 4      | Width    |     |      |      |
| 4      | Head     |     |      |      |
| 4      | Shoulder |     |      |      |
| 4      | Trunk    |     |      |      |
| 5      | Goal     |     |      |      |
| 5      | Width | 0.925926    |      |      |
| 5      | Head     |     |      |      |
| 5      | Shoulder |     |      |      |
| 5      | Trunk    |     |      |      |
</details>

