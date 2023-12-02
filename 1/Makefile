CC=g++
BUILDDIR=build
EXECUTABLE=day1

run: build
	$(BUILDDIR)/$(EXECUTABLE)

build: solution.cpp builddir
	g++ ./solution.cpp -o $(BUILDDIR)/$(EXECUTABLE)

builddir:
	mkdir -p $(BUILDDIR)