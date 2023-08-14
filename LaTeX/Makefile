SHELL := /bin/bash

targets = UNIT1-Introduction.pdf UNIT2-Statistical-Learning.pdf UNIT3-MC-Methods.pdf UNIT4-Unsupervised-Learning.pdf UNIT5-Regression.pdf UNIT6-Regularization-and-Kernel-Methods.pdf UNIT7-Classification.pdf UNIT8-Decision-Trees.pdf UNIT9-Neural-Networks.pdf

targets = UNIT1-Introduction.pdf 


all: $(targets)
$(targets): %.pdf: %.tex
	lualatex $<

clean:
	rm -f *.{bcf,run.xml,pro,aux,nav,out,log,idx,ind,ilg,toc,bbl,blg,tdo,lot,lof,glo,snm}

cleanpdf:
	rm -f ${targets}

