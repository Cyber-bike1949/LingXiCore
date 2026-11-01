# LingXi Core 5.0

插件产品与远程设备产品的共用库，不是独立应用。包含 TypeScript 帧协议、配对/身份模型、文件操作类型，以及 Rust 文件操作实现。来源为 LingXi1949 4.0 实现，保留 GPL-3.0 许可。

产品通过 vendor/lingxi-core 固定源码快照引用，无需联网或相邻仓库。运行 `python3 scripts/sync-consumer.py /path/to/product` 更新指定产品；脚本写入包含来源提交和逐文件 SHA-256 的 SOURCE.json。产品应一起评审快照变化，但可以独立构建和发布。

平台扩展落在各产品的进程、Shell、安装器和原生传输绑定；不要把 Obsidian UI 或平台安装流程放入本库。
