def hello_world():
    """
    MCP GitHub工具测试函数
    """
    print("Hello, World! This is a test for MCP GitHub tools.")
    return "测试成功"

def add_numbers(a, b):
    """
    简单的加法函数，用于测试
    """
    return a + b

def main():
    """
    主函数
    """
    result = hello_world()
    sum_result = add_numbers(10, 20)
    print(f"加法结果: {sum_result}")
    return result

if __name__ == "__main__":
    main()