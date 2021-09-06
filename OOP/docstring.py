# docstring

def find_suggestion_videos(self, number_of_suggestions=5):
    # Google docstring:
    """유저에게 추천할 영상을 찾아준다
    Parameters:
      number_of_suggestions (int): 추천하고 싶은 영상 수
        (기본값은 5)
        
    Returns:
      list: 추천할 영상 주소가 담긴 리스트
    """
    
    # reStructuredText(파이썬 공식 문서화 기준):
    """유저에게 추천할 영상을 찾아준다
    
    :param number_of_suggestions: 추천하고 싶은 영상 수
      (기본값은 5)
    :type number_of_suggestions: int
    :returns: 추천할 영상 주소가 담긴 리스트
    :rtype: list
    """
    
    # NumPy/SciPy (통계, 과학 분야에서 쓰이는 Python 라이브러리):
    """유저에게 추천할 영상을 찾아준다
    
    Parameters
    ----------
    number_of_suggestions: int
      추천하고 싶은 영상 수 (기본값은 5)
        
    Returns
    -------
    list 
      추천할 영상 주소가 담긴 리스트
    """