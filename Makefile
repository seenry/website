all: index

index:
	@python gen.py > index.html
	@cp -r ./* ../public_html/
	@rm ../public_html/gen.py
	@rm ../public_html/idx.html
	@rm ../public_html/index.oe
	@rm ../public_html/Makefile

.PHONY: all clean

clean:
	rm -rf index.html

