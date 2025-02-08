# Methods Table Generator

Bu Python programı, **list, set, string, tuple ve dictionary** veri tiplerine ait tüm metotları bir CSV dosyasında tablo formatında saklar.

## 🚀 Özellikler
- Python'un temel veri tiplerinin metotlarını listeler.
- **Gizli metotları ("__" ile başlayanları) hariç tutar.**
- Tüm metotları `methods.csv` dosyasına düzgün bir formatta yazar.

## 📌 Kullanım
1. **Python 3 yüklü olmalıdır.**
2. Terminal veya Komut Satırında aşağıdaki komutu çalıştırın:
   ```sh
   python methods_list.py
   ```
3. **methods.csv** dosyası oluşturulacaktır.
4. Dosyayı açarak listelenen metodları inceleyebilirsiniz.

## 📂 Çıktı Formatı (methods.csv)
| List Methods | Set Methods | String Methods | Tuple Methods | Dictionary Methods |
|-------------|------------|---------------|--------------|-------------------|
| append | add | capitalize | count | clear |
| clear | clear | casefold | index | copy |
| copy | copy | center |  | fromkeys |
| ... | ... | ... | ... | ... |

## Gerekli Kütüphaneler
Kodun çalışması için **csv** modülü gereklidir. Ancak, Python’un standart kütüphanesi olduğu için ekstra yükleme yapmanıza gerek yoktur.

## 📝 VS Code'da Markdown Önizleme
VS Code kullanıyorsanız, README.md dosyasını açtıktan sonra şu kısayolu kullanarak önizleme yapabilirsiniz:

```sh
CTRL + Shift + V
```

---

Bu proje, Python'un veri yapılarını ve metotlarını öğrenmek isteyenler için faydalıdır. Katkıda bulunmak isterseniz, **Pull Request** gönderebilirsiniz! 😊

