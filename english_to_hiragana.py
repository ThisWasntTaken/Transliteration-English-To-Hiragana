def transliterate_english_to_hiragana(s):
    mapping = {" " : " ", "sokuon" : u"\u3063",\
        "small_a" : u"\u3041", "a" : u"\u3042",\
        "small_i" : u"\u3043", "i" : u"\u3044",\
        "small_u" : u"\u3045", "u" : u"\u3046",\
        "small_e" : u"\u3047", "e" : u"\u3048",\
        "small_o" : u"\u3049", "o" : u"\u304A",\
        "ka" : u"\u304B", "ki" : u"\u304D", "ku" : u"\u304F", "ke" : u"\u3051", "ko" : u"\u3053",\
        "ga" : u"\u304C", "gi" : u"\u304E", "gu" : u"\u3050", "ge" : u"\u3052", "go" : u"\u3054",\
        "sa" : u"\u3055", "shi" : u"\u3057", "su" : u"\u3059", "se" : u"\u305B", "so" : u"\u305D",\
        "za" : u"\u3056", "ji" : u"\u3058", "zu" : u"\u305A", "ze" : u"\u305C", "zo" : u"\u305E",\
        "ta" : u"\u305F", "chi" : u"\u3061", "tsu" : u"\u3064", "te" : u"\u3066", "to" : u"\u3068",\
        "da" : u"\u3060", "dzi" : u"\u3062", "dzu" : u"\u3065", "de" : u"\u3067", "do" : u"\u3069",\
        "na" : u"\u306A", "ni" : u"\u306B", "nu" : u"\u306C", "ne" : u"\u306D", "no" : u"\u306E",\
        "ha" : u"\u306F", "hi" : u"\u3072", "hu" : u"\u3075", "he" : u"\u3078", "ho" : u"\u307B",\
        "ba" : u"\u3070", "bi" : u"\u3073", "bu" : u"\u3076", "be" : u"\u3079", "bo" : u"\u307C",\
        "pa" : u"\u3071", "pi" : u"\u3074", "pu" : u"\u3077", "pe" : u"\u307A", "po" : u"\u307D",\
        "ma" : u"\u307E", "mi" : u"\u307F", "mu" : u"\u3080", "me" : u"\u3081", "mo" : u"\u3082",\
        "small_ya" : u"\u3083", "small_yu" : u"\u3085", "small_yo" : u"\u3087",\
        "ya" : u"\u3084", "yu" : u"\u3086", "yo" : u"\u3088",\
        "ra" : u"\u3089", "ri" : u"\u308A", "ru" : u"\u308B", "re" : u"\u308C", "ro" : u"\u308D",\
        "small_wa" : u"\u308E", "wa" : u"\u308F", "wi" : u"\u3090", "we" : u"\u3091", "wo" : u"\u3092",\
        "n" : u"\u3093", "vu" : u"\u3094"
        }
    
    s += " "
    out = ""
    curr_tok = ""
    prev_tok = ""
    for i in range(len(s)):
        if curr_tok in ["ch", "j", "sh"]:
            if s[i] in ["a", "u", "o"]:
                out += mapping[curr_tok + "i"] + mapping["small_" + "y" + s[i]]
            elif s[i] == "i":
                out += mapping[curr_tok + "i"]
            elif s[i] == "e":
                out += mapping[curr_tok + "i"] + mapping["small_e"]
            
            prev_tok = curr_tok + s[i]
            curr_tok = ""
            continue
        
        if curr_tok in ["ky", "ny", "hy", "by", "py", "my"]:
            if s[i] in ["a", "u", "o"]:
                out += mapping[curr_tok[0] + "i"] + mapping["small_" + curr_tok[1] + s[i]]
            elif s[i] in ["i", "e"]:
                out += mapping[curr_tok[0] + "i"] + mapping["small_" + s[i]]
            
            prev_tok = curr_tok + s[i]
            curr_tok = ""
            continue

        if curr_tok and s[i] == curr_tok[-1]:
            out += mapping["sokuon"]
        else:
            curr_tok += s[i]

        if curr_tok in mapping:
            if curr_tok == "n" and s[i + 1] in ["a", "i", "e", "u", "o"]:
                continue
            elif curr_tok == "n" and s[i + 1] not in ["a", "i", "e", "u", "o"]:
                out += mapping["n"]
            elif prev_tok and curr_tok == prev_tok[-1]:
                out += mapping["small_" + curr_tok]
            else:
                out += mapping[curr_tok]
            
            prev_tok = curr_tok
            curr_tok = ""
    
    return out[: -1]

if __name__ == "__main__":
    print("Enter text in English.")
    while True:
        s = input()
        print(transliterate_english_to_hiragana(s))