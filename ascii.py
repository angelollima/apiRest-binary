import string

def digits():
    digits = [i for i in range(5000)]
    return digits


def punctuation_methods():
    *punctuation_methods, = string.punctuation
    return punctuation_methods


def upper_lower_letters():
    *letters_lowercase, = string.ascii_lowercase
    *upper_lower_letters, = "".join(c + c.upper() for c in letters_lowercase)
    return upper_lower_letters


def words_accent():
    *words_accent, = "".join(c + c.upper() for c in """áâãàäåæāăąªçÇcĆčČďđĎĐéÉêÊèÈëËēĒėĖęĘěĚĕĔəƏģĢğĞíÍìÌîÎïÏīĪįĮıİķĶĺĹļĻľĽłŁñÑńŃņŅňŇóÓôÔõÕòÒöÖøØōŌőŐœŒŕŔřŘß§śŚšŠşŞþÞťŤțȚţŢúÚüÜùÙûÛūŪůŮűŰųŲũŨýÝźŹżŻžŽ""")
    return words_accent