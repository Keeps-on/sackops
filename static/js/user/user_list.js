layui.use(['layer', 'form', 'table', 'jquery', 'transfer'], function () {
    var $ = layui.$ //重点处
        , layer = layui.layer
        , form = layui.form
        , table = layui.table
        , transfer = layui.transfer;

    // 创建用户
    var createUrl = $("input[name='url_user_create']").val();
    // 用户列表
    var userUrl = $("input[name='url_user_list']").val();
    // 数据表格
    var dataUrl = $("input[name='url_user_data']").val();
    // 修改用户
    var updateUrl = $("input[name='url_user_update']").val();
    // 删除用户

    // 角色列表
    var roleUrl = $("input[name='url_role_data']").val();


    /**
     * 用户表格渲染
     */
    table.render({
        elem: '#user_table'
        , height: 420
        , url: dataUrl //数据接口
        , id: 'user' //数据接口
        , title: '用户表'
        , page: true //开启分页
        // , toolbar: 'default' //开启工具栏，此处显示默认图标，可以自定义模板，详见文档
        , toolbar: '#toolbarDemo'//开启自定义工具行，指向自定义工具栏模板选择器 https://www.jb51.net/article/170339.htm
        // , defaultToolbar: ['filter', 'print', 'exports']
        , totalRow: true //开启合计行
        , cols: [[ //表头
            {type: 'checkbox', fixed: 'left'}
            , {field: 'id', title: 'ID', sort: true, fixed: 'left', align: 'center', totalRowText: '合计：'}
            , {field: 'username', title: '用户名', align: 'center'}
            , {field: 'password', title: '密码', align: 'center'}
            // , {field: 'phone', title: '手机号码', align: 'center'}
            // , {field: 'email', title: '邮箱', align: 'center'}
            , {fixed: 'right', title: '操作', align: 'center', toolbar: '#barDemo'}
        ]]
    });


    /**
     * 表格监听事件
     */
    table.on('toolbar(user_action)', function (obj) {
        var checkStatus = table.checkStatus(obj.config.id)
            , data = checkStatus.data; //获取选中的数据
        switch (obj.event) {
            case 'user_create':
                layer.msg('添加');
                layer.open({
                    title: '在线调试'
                    // , area: ['500px', '300px']
                    , area: '600px'
                    , content: $('#user_popup').html()
                    , yes: function (index, layero) {
                        console.log('回调函数')
                        // 获取用户名
                        var username = $('#username').val();
                        // 获取密码
                        var password = $('#password').val();
                        //TODO 校验
                        $.get(createUrl, {username: username, password: password},
                            function (result) {
                                console.log(result)
                            })
                        console.log(username, password)

                        layer.close(index); //如果设定了yes回调，需进行手工关闭
                    }
                });
                break;
            case 'update':
                if (data.length === 0) {
                    layer.msg('请选择一行');
                } else if (data.length > 1) {
                    layer.msg('只能同时编辑一个');
                } else {
                    layer.alert('编辑 [id]：' + checkStatus.data[0].id);
                }
                break;
            case 'delete':
                if (data.length === 0) {
                    layer.msg('请选择一行');
                } else {
                    layer.msg('删除');
                }
                break;
        }
        ;
    });

    /**
     * 监听工具事件
     */
    table.on('tool(user_action)', function (obj) { //注：tool 是工具条事件名，test 是 table 原始容器的属性 lay-filter="对应的值"
        var data = obj.data //获得当前行数据
            , layEvent = obj.event; //获得 lay-event 对应的值
        if (layEvent === 'detail') {


            transfer.render({
                id: 'transfer_role' //定义索引
                , elem: '#transfer_role'
                , title: ['系统角色', '分配角色']
                , showSearch: true
                , parseData: function (data) {
                    return {
                        "value": data.id //数据值
                        , "title": data.name //数据标题
                        // , "disabled": res.disabled  //是否禁用
                        // , "checked": res.checked //是否选中
                    }
                }
                , data: []
                , value: []
                , onchange: function (obj, index) {

                    // // console.log(index)  // 返回0或者1
                    // // console.log(obj) // 返回数据
                    // var user_id = []    // 发送数据的
                    // for (var item in obj) {
                    //     var uid = obj[item].value;
                    //     user_id.push(uid)
                    // }
                    //
                    // if (index == 0) {
                    //     $.post(ConfigUrl, {index: 'add', user_id: user_id}, function (res) {
                    //         console.log(res)
                    //     });
                    // } else {
                    //     $.post(ConfigUrl, {index: 'remove', user_id: user_id}, function (res) {
                    //         console.log(res)
                    //     });
                    // }

                    console.log(user_id)


                }
            })


            layer.msg('查看操作');
        } else if (layEvent === 'del') {
            layer.confirm('真的删除行么', function (index) {
                obj.del(); //删除对应行（tr）的DOM结构
                layer.close(index);
                //向服务端发送删除指令
            });
        } else if (layEvent === 'edit') {
            // 获取用户id
            var user_id = data.id;
            // 获取用户名
            var username = data.username;
            // 获取密码
            var password = data.password;

            layer.open({
                title: '在线调试'
                // , area: ['500px', '300px']
                , area: '600px'
                , content: $('#user_popup').html()
                , success: function (layero, index) {
                    // 将数据进行填入到
                    $('#username').val(username);
                    $('#password').val(password);
                }
                , yes: function (index, layero) {

                    // 获取用户名
                    var username = $('#username').val();
                    // 获取密码
                    var password = $('#password').val();
                    // 发送请求
                    $.get(updateUrl, {user_id: user_id, username: username, password: password},
                        function (result) {
                            console.log(result)
                            // 表格重载
                            table.reload('user', {
                                page: {
                                    curr: 1
                                }
                            });
                        })


                    layer.close(index); //如果设定了yes回调，需进行手工关闭
                }
            });


            // layer.msg('编辑操作');
        }
    });

    layer.msg('Hello World');


    /**
     * 获取角色列表
     */
    function get_role_list() {
        var role_list = []
        $.get(roleUrl, {}, function (result) {
            var _list = result.data;
            console.log(_list)
            return _list
        })

        return role_list
    }

    console.log(get_role_list())


});






