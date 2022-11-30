if __name__ == "__main__":
    file_info = []
    print("StepPXX Lua Maker by Qwerty_")

    while True:
        desc = input("\n#DESCRIPTION의 내용을 입력해주세요 : ")
        default_file = input("음악 파일 위치를 입력해주세요 : ")
        file_info.append([desc, default_file])

        is_continue = input("다른 음악을 추가하시겠습니까?(y/n) : ")
        if is_continue.lower() == "y":
            continue
        else:
            break

    default_file = input("\n기본 음악 파일 위치를 입력해주세요 : ")
    file_info.append(["default", default_file])

    with open("default.lua", "w+") as f:
        f.write("local songDir = GAMESTATE:GetCurrentSong():GetSongDir()\n")
        f.write("local t, description = GAMESTATE:GetCurrentStepsCredits()\n\n")

        for i, info in enumerate(file_info):
            if i == 0:
                f.write(f'if description == "{info[0]}" then\n')
            elif i == len(file_info) - 1:
                f.write("else\n")
            else:
                f.write(f'elseif description == "{info[0]}" then\n')

            f.write("    return Def.Sound {\n")
            f.write(f'        File = (songDir .. "{info[1]}"),\n')
            f.write(
                """        OnCommand = function(self)
            self:play()
        end
    }\n"""
            )
        f.write("end")

    print("\ndefault.lua 파일이 생성되었습니다.\nlua폴더에 추가해주세요.")
    input()
