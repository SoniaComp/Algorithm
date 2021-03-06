'''
폴더 안에 __init__.py 파일이 있으면 해당 폴더는 패키지로 인식됩니다. 그리고 기본적으로 __init__.py 파일의 내용은 비워둘 수 있습니다. 
(파이썬 3.3 이상부터는 __init__.py 파일이 없어도 패키지로 인식되지만 __init__.py를 사용할 것을 권장)

- calcpkg
  ⎿ __init__.py
  ⎿ operation.py
  ⎿ geometry.py

패키지의 모듈에서는 __name__변수에 패키지. 모듈 형식으로 이름이 들어갑니다.


<< 가상환경을 만들어서 모듈과 패키지 관리하기 >>
독립된 공간을 만들어서, 패키지 목록 관리