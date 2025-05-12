# LECTURE NOTES

## 26.02
Midtermde namespace sorusu kesin olacak.

## 03.03 4-1
Complexity
![alt text](images\image.png)


## 05.03 4-2
Hoca binary search anlattı. Complexity si logaritmik (log2 tabanında n)
big O için log basei önemli mi? Düşün Değil çünkü taban işlemleri ile asimptotik olarak aynı olduğunu gösterebiliriz.

### OBJECT ORIENTED PYTHON IMPLEMENTATION
#### Classes

Fonksiyon sadece çağrılınca kednine ait namespacei açılıyor ve execute edildikten sonra garbage collectora gider.
Class ile function arasındaki fark class içerisi execute ediliyor. Function çağrılana kadar edilmez. Ayroca class namespace function gibi kullanıldıktan sonra silinmez. 

***Çağrılmadığı müddetçe functionın namespacei yok, function call un namespacesi var.***

## 10.03 5-1
Class is a collection of variables & functions.

### **Namespace Example**: 

i - 5  
f ( ) - ... "Description of function"  
Apple - **New namespace**   
x - **x object namespace** (X is an apple -- *x is an instance object.*)  

**New namespace:**  (*class objects*)  
type - fruit  
location - tree  
drop(pp) - ... "Description of function"

![alt text](images\image2.jpeg)

## 12.03 5-2
Pazartesi quiz var. Logaritmik kompleksite sorusu da olacak.  

## 12.05 Last Lecture
Array vs List: Çalışma süreleri hemen hemen aynı, ramde teleport özelliği var. Array cache kullanılabilir. Cache performansı biraz probabilsitic. Data structure içine objelerin referansı konuyor. Objeler aslında oldukları yerde kalıyorlar. Data structure data tutmaz, onları düzenler.

List bir head ile define edilir. Head bir list itemdır (İlk list item). 
Removal da list iyi değil, bulması zor, bulunduktan sonrası kolay bulması O n silmesi O 1 totalde O n. Transactional şeyler de list iyi (yani removal çok gerekmiyor).

Remove array index kaydırma ile yapılıyor. O(n)  Removal için de array iyi değil. Indexle işlem çok kolay.

Removal için binary tree - b tree iyi. O(logn) B tree'nin pageleri array.

herhangi bir treede herhangi bir sayıdan büyük en küçük sayıyı nasıl bulursun benzeri bir soru kesin gelir!! o sayıyı bul sağına git sonra sol sol sol

tree yi breath first print edelim

tree yi yan yatmış şekilde print edelim



## finalde:

diyelim ki mağazadasın, card transaction tutman lazım vergi memuru gelip şu tarihteki transactionu göster diyor. Nasıl bir data structure önerirsin?  Birden çok data structure önerisi bekliyor hoca. Find için tree normalde list tavsiye edilebilir.









