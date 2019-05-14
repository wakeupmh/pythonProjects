from PIL import Image
import os
def main():
    ext = input("extension of image:")
    size = float(input("Size to resize:"))
    resize(ext, size)
def resize(ext, size):
    dirImg = './imgs'
    lDir = os.listdir(dirImg)
    for f in lDir:
        if (f.endswith('.' + ext)):
            img = Image.open('imgs/' + f)
            fn, fext = os.path.splitext(f)
            # print(os.path.exists(os.path.dirname('{}/{:.0f}'.format(dirImg,size))))
            if not os.path.exists(os.path.dirname('imgs/{:.0f}/'.format(size))):
                os.mkdir('./imgs/{:.0f}/'.format(size))
            img.thumbmail = (size, size)
            img.save('imgs/{:.0f}/{}_{:.0f}{}'.format(size, fn, size, fext))
    print("Resized successfully!!!!")

if __name__ == "__main__":
    main()
