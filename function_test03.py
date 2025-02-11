def judge_grade(grade):
    """
    成績（grade）が与えられたとき、以下の条件に基づいて、成績評価を返す関数を作成してください。

    90点以上なら、'優秀です'と return
    80点以上、90点未満なら、'良いです'と return
    70点以上、80点未満なら、'可もなく不可もなく'と return
    70点未満なら、 '改善が必要です'と return
    """

    if grade >= 90:
        return '優秀です'
    elif  80 <= grade < 90:
        return '良いです'
    elif 70 <= grade < 80:
        return '可もなく不可もなく'
    elif grade < 70:
        return '改善が必要です'