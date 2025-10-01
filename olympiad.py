scores = list(map(int, input('Рейтинговый список: ').split()))
student_score = int(input('Балл Стаса: '))

sort_scores = sorted(scores, reverse=True)


def check_winners(scores, student_score):
    for i in range(3):
        if scores[i] == student_score:
            print('Вы в тройке победителей!')
            return None
    print('Вы не попали в тройку победителей.')


check_winners(sort_scores, student_score)

# test commit