## From time to time, if jupyter notebook not closed correctly --> ls takes forevor in the directory

## First identify the port used 
jupyter notebook list
## Trovata la porta trova il PID e killa il processo
kill -9 `lsof -n -i4TCP:8888 | grep jupyter | cut -f2 -d " "`
