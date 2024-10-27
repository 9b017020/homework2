import sys

# 存儲人員資料的列表
records = []

# 主選單
def main_menu():
    while True:
        print()
        print("--- 人事資料管理系統 ---")
        print("1. 新增資料")
        print("2. 查詢資料")
        print("3. 修改資料")
        print("4. 刪除資料")
        print("5. 顯示所有資料")
        print("6. 退出系統")
        print("------------------------")

        choice = input("請選擇功能:")

        if choice == '1':
            add_record()
        elif choice == '2':
            search_record()
        elif choice == '3':
            modify_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            display_all_records()
        elif choice == '6':
            sys.exit("系統已退出")
        else:
            print("無效選項，請重新選擇。")

# 新增資料
def add_record():
    while True:
        department = input("輸入部門: ")
        name = input("輸入姓名: ")
        age = input("輸入年齡: ")
        phone = input("輸入手機: ")

        record = {"部門": department, "姓名": name, "年齡": age, "手機": phone}
        records.append(record)

        cont = input("是否繼續新增資料？(y/n): ")
        if cont.lower() != 'y':
            break

# 查詢資料
def search_record():
    name = input("輸入查詢的姓名: ")
    found = False

    for record in records:
        if record["姓名"] == name:
            found = True
            print("--- 查詢結果 ---")
            print("{:<10} {:<10} {:<10} {:<15}".format("部門", "姓名", "年齡", "手機"))
            print("------------------------------------------------")
            print("{:<10} {:<10} {:<10} {:<15}".format(
                record["部門"], record["姓名"], record["年齡"], record["手機"]
            ))
            break

    if not found:
        print("查無此人")

# 修改資料
def modify_record():
    name = input("輸入要修改的姓名: ")
    found = False

    for record in records:
        if record["姓名"] == name:
            found = True
            print("\n找到的資料：")
            print("{:<10} {:<10} {:<10} {:<15}".format("部門", "姓名", "年齡", "手機"))
            print("------------------------------------------------")
            print("{:<10} {:<10} {:<10} {:<15}".format(
                record["部門"], record["姓名"], record["年齡"], record["手機"]
            ))

            # 修改選項
            print("\n1. 修改部門")
            print("2. 修改姓名")
            print("3. 修改年齡")
            print("4. 修改手機")
            choice = input("請選擇要修改的欄位: ")

            if choice == '1':
                new_value = input("請輸入新的部門: ")
                record["部門"] = new_value
            elif choice == '2':
                new_value = input("請輸入新的姓名: ")
                record["姓名"] = new_value
            elif choice == '3':
                new_value = input("請輸入新的年齡: ")
                record["年齡"] = new_value
            elif choice == '4':
                new_value = input("請輸入新的手機: ")
                record["手機"] = new_value
            else:
                print("無效選項，請重新選擇。")
                continue

            print("\n--- 更新後的資料 ---")
            print("{:<10} {:<10} {:<10} {:<15}".format("部門", "姓名", "年齡", "手機"))
            print("------------------------------------------------")
            print("{:<10} {:<10} {:<10} {:<15}".format(
                record["部門"], record["姓名"], record["年齡"], record["手機"]
            ))
            break

    if not found:
        print("查無此人")

# 刪除資料
def delete_record():
    name = input("輸入要刪除的姓名: ")
    found = False

    for i, record in enumerate(records):
        if record["姓名"] == name:
            found = True
            print("\n找到的資料：")
            print("{:<10} {:<10} {:<10} {:<15}".format("部門", "姓名", "年齡", "手機"))
            print("------------------------------------------------")
            print("{:<10} {:<10} {:<10} {:<15}".format(
                record["部門"], record["姓名"], record["年齡"], record["手機"]
            ))

            confirm = input("確定要刪除該人員資料嗎？(y/n): ")
            if confirm.lower() == 'y':
                records.pop(i)
                print(f"{name}的資料已刪除。")
                print("--- 剩餘的所有資料 ---")
                display_all_records()
            break

    if not found:
        print("查無此人")

# 顯示所有資料
def display_all_records():
    if not records:
        print("目前沒有任何資料")
    else:
        print("{:<10} {:<10} {:<10} {:<15}".format("部門", "姓名", "年齡", "手機"))
        print("------------------------------------------------")
        for record in records:
            print("{:<10} {:<10} {:<10} {:<15}".format(
                record["部門"], record["姓名"], record["年齡"], record["手機"]
            ))

# 執行主程式
if __name__ == "__main__":
    main_menu()
