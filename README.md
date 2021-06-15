# wa-tools

## Create an input file

To find out how to get your inputfile.txt, follow this guide, but instead of copying outer html copy the inner HTML so you'll get a single string with comma seperated names/numbers. Then copy it into a text file instead of excel or csv.
▶️ [Guide](https://mashtips.com/whatsapp-group-extract-contact/)



| :warning: WARNING       |
|:---------------------------|
| Be aware that you will need to probably still manually select the tags when copying the result to WhatsApp and that if you have the contacts saved with multiple names only the first names will be in the extracted line. Since it is your whatsapp one line and the end will be `@You`, you will need to replace it with your own name or number but it will not display as tag or you remove it altogether. |

## Run the script

`python tagify.py -i example.txt -o tags.txt`

or 

`python tagify.py` which will ask for a string to enter as input and create a default `tags.txt`

Copy your result from tags.txt or from the command line output and into WhatsApp.

