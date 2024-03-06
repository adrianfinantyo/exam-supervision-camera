# NOTES

## Epoch

Penentuan jumlah epoch yang optimal adalah dengan melihat grafik loss dan accuracy. Jika grafik loss sudah mendekati 0 dan grafik accuracy sudah mendekati 1, maka epoch sudah optimal.

## Confusion Matrix

| Status   | Description     |
| -------- | --------------- |
| POSITIVE | Mencontek       |
| NEGATIVE | Tidak Mencontek |

- TP = Siswa mencontek yang benar terdeteksi sebagai mencontek
- TN = Siswa tidak mencontek yang benar terdeteksi sebagai tidak mencontek
- FP = Siswa tidak mencontek yang terdeteksi sebagai mencontek
- FN = Siswa mencontek yang terdeteksi sebagai tidak mencontek

### Prioritization

- Lebih baik FP dari pada FN
- Semaksimal mungkin menghindari FN

Dengan prioritas tersebut dan ditinjau dari formula precision dan recall, maka ukuran yang akan diperhatikan adalah recall. Recall adalah ukuran yang menunjukkan seberapa banyak data positif yang terdeteksi dengan benar.

![](https://www.kdnuggets.com/wp-content/uploads/selvaraj_confusion_matrix_precision_recall_explained_12.png)

## F1 - Confident Score

F1 score adalah rata-rata harmonik dari precision dan recall. F1 score adalah ukuran yang baik untuk mengevaluasi model ketika kelas target tidak seimbang.

Confident score adalah nilai yang menunjukkan seberapa yakin model dalam memprediksi suatu kelas. Semakin tinggi confident score, semakin yakin model dalam memprediksi kelas tersebut.

Output yang diharapkan adalah F1 score yang stabil pada confident score tertentu. Jika F1 score menurun ketika confident score meningkat, maka model tersebut tidak baik.

### Literature

- [https://serokell.io/blog/a-guide-to-f1-score](https://serokell.io/blog/a-guide-to-f1-score)
- [https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall)
