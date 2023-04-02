pycco:
	pycco -p -i -d annotated-sources v1-simple/

clean:
	rm -f $(shell find . -name '*~' -o -name '*.bak')
distclean: clean
	rm -rf annotated-sources
