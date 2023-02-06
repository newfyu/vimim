### 功能：

Vim在中文输入后，切换回normal模式时候不会自动回到英文输入法。这是vim的一大痛点。

目前有许多本地利用插件自动切换的解决方案。比如[GitHub - lipingcoding/autoim.vim: Vim 自动切换输入法](https://github.com/lipingcoding/autoim.vim)。但是对远程SSH使用的vim无效。

也有方案（[GitHub - lxyoucan/sshim.vim: ssh 远程vim,本地输入法自动切换插件](https://github.com/lxyoucan/sshim.vim)）利用本地服务器，通过网络接收信息的方案解决远程vim自动切换输入法的问题。但略显复杂。

这儿换了一个简单的思路，简单写了一个python脚本。在中文输入法的情况下，快速点击两下ESC返回normal模式后会回到英文输入法。不受远程和本地的限制，也不需要vim的插件。

脚本只有几行，非常简单，直接运行即可。如果需要后台运行和开机启动（针对mac os），可以把run_vimim.py添加到设置-登录项。同时要在设置-隐私与安全-辅助功能，设置-隐私与安全-输入监控中打开对应的开关。

脚本里面默认切换输入法是ctrl+space，如果是其他键位可以自行修改。
