# task1
echo "192.168.1.001,256.300.1.1" | grep -P '(((1=?\d{0,2})|(25=?[0-4])|(2[0-4]=?\d)|([2-9]=?\d{0,1})|(0=?\d?[1-9]))\.){3}((1=?\d{0,2})|(25=?[0-4])|(2[0-4]=?\d)|([2-9]=?\d{0,1})|(0=?\d?[1-9]))'
# task2
echo "site.png,site.com,csdzk.jpg" |grep -P '(\w+\.(png|jpg|gif))'
echo "https://site.png,site.com/folder/1.png,https://site.com/folder/1.exe,https://site.com/folder/1.png" | grep -P '(http[s]?:\/\/)?([\w]+\.[\w]{2,}\/[^,]+)(\.png|jpg|gif)'


# task4
echo -e "http://site.com/folder.sh/1.jpg \nhttp://site.com/folder/folder/1.exe\nsite.com/folder/folder/1.sh " | grep -P '^(http[s]?:\/\/)?[\w]+\w{2,}(\/?((?!\.sh).)*\/)?((?!\.sh).)*$'
