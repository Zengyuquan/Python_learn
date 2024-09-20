def print_file_info(file_name):

    f = None

    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print("文件的全部内容如下：")
        print(content)
    except Exception as e:
        print(f"出现出现异常了，原因是：{e}")
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    f = open(file_name,"a",encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == "__main__":
    print_file_info("D:/abc.txt")
    append_to_file("D:/abcd.txt","ddddd")