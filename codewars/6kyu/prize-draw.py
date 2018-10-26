# # https://www.codewars.com/kata/prize-draw/train/python
# def rank(st, we, n):
#     if not st:
#         return "No participants"
#
#     participants = st.split(',')
#     if n > len(participants):
#         return 'Not enough participants'
#
#     participants_lower = list(map(lambda p: p.lower(), participants))
#     participants_values = [sum([ord(c) - 96 for c in participant]) for participant in participants_lower]
#
#     winning_numbers = []
#     for a, b, c in zip(participants, participants_values, we):
#         winning_numbers.append((len(a) + b * c)
#
#         sorted_winners_by_name = sorted(zip(participants, winning_numbers), key=lambda n: n[0])
#         sorted_winners_by_value = sorted(sorted_winners_by_name, key=lambda n: n[1]
#         reverse = True)
#
#         return sorted_winners_by_value[n - 1][0]
#
#
