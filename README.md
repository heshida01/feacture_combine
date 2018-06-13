# feacture_combine
1. mergeDF：Support for output format of arff( numeric) and libsvm
  1)numeric:
   usage: python3 mergeDF.py inputfile1 inputfile2 outfile3 arff
   example: python3 mergeDF.py 20.arff 188.arff  arff

  2)libsvm:
   usage: python3 mergeDF.py inputfile1 inputfile2 outfile3 libsvm
   example: python3 mergeDF.py 20.libsvm  188.libsvm  208.libsvm

2. mergeDF_enum:Support for output format of arff (nominal) 
   usage: python3 mergeDF_enum.py inputfile1 inputfile2 outfile3 
   example: python3 mergeDF_enum.py weather.numeric1.arff  weather.numeric1.arff  weather.out.arff
  
Note:
  please use them in python3 environment
  if you have any questions please feel free to contact me(347547551@qq.com)
