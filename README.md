### 功能：

Vim在中文输入后，切换回normal模式时候不会自动回到英文输入法。这是vim的一大痛点。

目前有许多本地利用插件自动切换的解决方案。比如[GitHub - lipingcoding/autoim.vim: Vim 自动切换输入法](https://github.com/lipingcoding/autoim.vim)。但是对远程SSH使用的vim无效。

也有方案（[GitHub - lxyoucan/sshim.vim: ssh 远程vim,本地输入法自动切换插件](https://github.com/lxyoucan/sshim.vim)）利用本地服务器，通过网络接收信息的方案解决远程vim自动切换输入法的问题。但略显复杂。

这儿换了一个简单的思路，简单写了一个python脚本。在中文输入法的情况下，快速点击两下ESC返回normal模式后会回到英文输入法。不受远程和本地的限制，也不需要vim的插件。

脚本只有几行，非常简单，直接运行即可。如果需要后台运行和开机启动，可以修改附带plist里面的python和脚本存放路径，然后把vimim.plist文件放入~/Library/LaunchAgents。命令行`launchctl load -w ~/Library/LaunchAgents/vimim.plist`启动即可后台运行和开机自启动。

脚本里面默认切换输入法是ctrl+space，如果是其他键位可以自行修改。
