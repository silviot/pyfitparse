CC = gcc
CFLAGS = -I../../ -I./

decode: decode.o fit.o fit_convert.o fit_crc.o fit_product.o
	$(CC) $(CFLAGS) -o decode decode.o fit.o fit_convert.o fit_crc.o fit_product.o

%.o: ../../%.c
	$(CC) $(CFLAGS) -O -c $<

decode.o:
	$(CC) $(CFLAGS) -O -c decode.c


clean:
	rm -f decode decode.o fit.o fit_convert.o fit_crc.o fit_product.o
