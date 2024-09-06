# # 1 Ошибка при вызове inner_function()

# def test_function():
#     def inner_function():
#         print("Я в области видимости функции test_function")
#     inner_function()
#
# test_function()
# inner_function()


# 1  inner_function() назначена в глобальное пространство и видима при вызове
def test_function():
    global inner_function
    def inner_function():

        print("Я в области видимости функции test_function")
    inner_function()

test_function()
inner_function()