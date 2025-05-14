import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd


class EnergyStorageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("多应用情境下新型储能技术评估系统")
        self.root.geometry("1000x700")

        # 初始化示例数据
        self.technologies = [  "超级电容器", "铁铬液流电池", "钒氧化还原液流电池",   "锌溴液流电池",  "锌铁液流电池",  "锌镍氧化物液流电池",  "氢储能",
                               "超级电池",    "铅碳电池",  "阀控式铅酸蓄电池",   "锂聚合物电池",  "钛酸锂离子电池",   "磷酸铁锂电池",       "锂镍钴铝电池",
                               "锂镍锰钴电池",  "镍镉电池",  "镍铁电池",    "钠离子电池",  "氯化钠镍电池",    "钠-硫电池",  "锌空气电池",
                               "锌锰氧化物电池", "压缩空气储能", "飞轮储能", "冰储能", "液态空气储能", "冷冻水储能","熔盐储能"  ]
        self.applications = ["一次调频", "二次调频", "电压支持", "爬坡辅助", "黑启动",
            "稳定阻尼控制", "电能质量保障", "能源套利", "可再生能源时移", "三次调频",
            "延缓输配电设备扩容", "缓解输电阻塞", "电费管理", "备用电源", "季节性储能"]
        self.scores = pd.DataFrame({
            "一次调频": [0.11742 ,	0.23584 ,	0.28256 ,	0.27035 ,	0.29438 ,	0.27664 ,	1.17225 ,	0.09251 ,	0.15874 ,	0.11776 ,	0.30990 ,	0.29723 	,0.40074 ,	0.35966 ,	0.44000 ,	0.38610 ,	0.00000 ,	0.00000 ,	1.00916 ,	0.27809 ,	0.26258 ,	0.00000 ,	0.00000 ,	1.54758 ,	0.00000 ,0.00000 ,	0.27495 ,	0.00000 ],
            "二次调频": [0.00000, 	0.00000 ,	0.38047 ,	0.32021 ,	0.00000 ,	0.33699 ,	0.00000 ,	0.00000 ,	0.25012 ,	0.00000 ,	0.45050 ,	0.44083 ,	0.63179 ,	0.63915 ,	1.08091 ,	0.63501 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.30337 ,	0.35395 	,0.41174 ,	0.33370 ,	1.38935 ,	0.49525 ,	1.01240 ,	0.00000 ,	0.44502 ],
            "电压支持": [0.11711 ,	0.24331 ,	0.28993 ,	0.27520 ,	0.29966 ,	0.28160 ,	1.17225 ,	0.00000 ,	0.16163 ,	0.12030 ,	0.31350 ,	0.30376 	,0.40788 ,	0.36439 ,	0.00000 ,	0.39400 ,	0.00000 ,	0.00000 ,	1.00916 ,	0.28123 ,	0.26770 ,	0.00000 	,0.00000 ,	1.54758 ,	0.00000 ,	0.00000 ,	0.28210 ,	0.00000 ],
            "爬坡辅助": [0.11065 ,	0.20819 ,	0.26898 ,	0.21926 ,	0.23494 ,	0.22362 	,1.03175 ,	0.08629 ,	0.15286 ,	0.11931, 	0.30913 ,	0.30070 ,	0.38925 ,	0.35157 ,	0.42716 ,	0.38213 ,	0.00000 ,	0.00000 ,	0.36688 	,0.21993 ,	0.21904 	,0.28057 ,	0.19504 ,	1.54517 ,	0.20000 ,	0.31893 ,	0.23012 	,0.18370 ],
            "黑启动": [0.09150 	,0.10586 ,	0.29996 ,	0.14593 ,	0.15279 ,	0.14792 ,	0.17788 ,	0.05933 ,	0.09064 ,	0.05855 ,	0.57736 ,	0.55475 ,	0.66225 ,	0.73763 ,	1.01717 	,0.77194 ,	1.06459 ,	1.52779 ,	0.41888 ,	0.16030 ,	0.13325 ,	0.14827 ,	0.06924 ,	0.00000 ,	0.08850 ,	0.27436 ,	0.13376 ,	0.14464 ],
            "稳定阻尼控制": [0.00000 ,	0.00000 ,	1.20159 ,	0.46415 ,	0.00000 ,	0.59364 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 	,0.00000 ,	1.08790 ,	0.00000 ,	0.00000 ,0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 	,0.00000 ,	0.00000 ,	1.53033 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ],
            "电能质量保障": [0.10770 ,	0.20224 ,	0.26497 ,	0.21260 ,	0.22744 ,	0.21673 ,	1.02310 ,	0.08425 ,	0.14886 ,	0.11637 ,	0.30697 ,	0.29948 ,	0.38620, 	0.34885 ,	0.42470 ,	0.38000 ,	0.49314 ,	1.20674 ,	0.35717 ,	0.21292 ,	0.21222 ,	0.26545 ,	0.00000 ,	1.54716 ,	0.00000 ,	0.00000 ,	0.22318 ,	0.00000 ],
            "能源套利": [0.00000 ,	0.13930 ,	0.41143 ,	0.17568 ,	0.21388 ,	0.14354 ,	1.18613 ,	0.21104 ,	0.12664 ,	0.07456 ,	0.59291 ,	0.57598 ,	0.67461 ,	0.69256 	,1.02341 ,	0.00000 ,	1.22103 ,	1.52779 ,	0.45493 ,	0.00000 ,	0.08762 ,	0.00000 ,	0.08445, 	0.00000 ,	0.08478 ,	0.27914 ,	0.13435 ,	0.16288 ],
            "可再生能源时移": [0.00000 ,	0.13930 ,	0.41143 ,	0.17568 ,	0.21388 ,	0.14354 ,	0.14765, 	0.21104 ,	0.12664 ,	0.07456 ,	0.59291 ,	0.57598 ,	0.67461 ,	0.69256 ,	1.01717 ,	0.00000 ,	1.20721 ,	1.52779 ,	0.45493, 	0.00000 ,	0.08762 ,	0.00000 ,	0.08445 ,	0.00000 ,	0.08478 ,	0.27914 ,	0.13435 ,	0.16288 ],
            "三次调频": [0.00000 ,	0.00000 ,	0.59161 ,	0.25642 ,	0.00000 ,	0.23101 ,	0.31637 ,	0.00000, 	0.16839 ,	0.09355 ,	0.86602 ,	1.19609 ,	1.12518 ,	0.88561 	,1.06989 ,	0.00000 ,	0.00000 ,	0.00000 ,	1.12852 ,	0.00000 ,	0.15519 ,	0.22488 	,0.11676 ,	0.00000 ,	0.13964 ,	0.49906 ,	0.23097 ,	0.26127 ],
            "延缓输配电设备扩容": [0.00000 ,	0.18688 ,	0.67883 ,	0.26768 ,	0.30809 	,0.23741, 	0.24414 ,	0.32029 ,	0.16817 ,	0.09988 ,	0.86602 ,	1.19827 ,	1.11808 ,	0.94037 ,	1.03903 ,	0.00000 ,	0.00000 ,	0.00000 ,	1.12852 ,	0.00000 ,	0.16541 ,	0.27208 ,	0.12240 ,	0.00000 ,	0.12365 ,	0.44560 ,	0.20575 ,	0.23011 ],
            "缓解输电阻塞": [0.00000 ,	0.00000 ,	0.62935 ,	0.25711 	,0.00000 ,	0.23223 ,	0.00000 ,	0.00000 ,	0.17805 ,	0.00000 ,	0.85181, 	1.20138 ,1.12600 ,	0.87343 ,	1.08313 ,	0.00000 ,	0.00000 ,	0.00000 ,	1.12852 ,	0.00000 ,	0.16107 ,	0.22243 ,	0.11874 ,	0.00000 ,	0.14590 ,	0.55283 	,0.00000 ,	0.28266 ],
            "电费管理": [0.17803 ,	0.13211 ,	0.18379 ,	0.14914 ,	0.16662 ,	0.14217 ,	1.03175 ,	0.11241 ,	0.10819 ,	0.08033 ,	0.19237 ,	0.18252 ,	0.23579 ,	0.20705 ,	0.21519 ,	0.21297 ,	0.30560 ,	1.21055 ,	0.26046 ,	0.14570 ,	0.12138, 	0.18557 ,	0.12895 ,	1.54663 ,	0.11301 ,	0.19475 ,	0.13841 ,	0.10453 ],
            "备用电源": [0.00000, 	0.13401 ,	0.18545 ,	0.14926 ,	0.16832 ,	0.14137 ,	1.03175 ,	0.10915 ,	0.10936 ,	0.08114 ,	0.19040 ,	0.18215 ,	0.23385 ,	0.20477 ,	0.21312 ,	0.00000 ,	0.30651 ,	1.21055 ,	0.25881 ,	0.14487 ,	0.12102 ,	0.18290 ,	0.12949 ,	1.54640 ,	0.11276 ,	0.19431 ,	0.13814 ,	0.10700 ],
            "季节性储能": [0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	1.76212 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 	,0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.00000 ,	0.06881 	,0.00000 ,	0.00000 ,	1.70354 ,	0.00000 ,	1.01500 ],
        }, index=self.technologies)

        # 样式配置
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TButton", padding=6, font=("微软雅黑", 10))
        self.style.map("TButton",
                       foreground=[('active', 'white'), ('!active', 'black')],
                       background=[('active', '#0052cc'), ('!active', '#e1e1e1')]
                       )

        # 主界面布局
        self.create_widgets()

    def create_widgets(self):
        # 顶部标题
        header = ttk.Frame(self.root)
        header.pack(pady=20, fill=tk.X)
        ttk.Label(header, text="多应用情境下新型储能技术评估系统",
                  font=("微软雅黑", 16, "bold"),
                  foreground="#0052cc").pack()

        # 应用选择区域
        selection_frame = ttk.LabelFrame(self.root, text="1. 选择应用情境")
        selection_frame.pack(padx=20, pady=10, fill=tk.X)

        self.app_vars = []
        for idx, app in enumerate(self.applications):
            var = tk.BooleanVar()
            cb = ttk.Checkbutton(selection_frame, text=app, variable=var)
            cb.grid(row=idx // 2, column=idx % 2, sticky=tk.W, padx=10, pady=5)
            self.app_vars.append((app, var))

        # 时间输入区域（动态生成）
        self.input_frame = ttk.LabelFrame(self.root, text="2. 设置时间分配")
        self.input_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # 结果展示区域
        result_frame = ttk.Frame(self.root)
        result_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(result_frame, columns=("score",),
                                 show="headings", height=6)
        self.tree.heading("#0", text="储能技术")
        self.tree.heading("score", text="综合得分")
        self.tree.column("#0", width=200)
        self.tree.column("score", width=150)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # 操作按钮
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="筛选技术",
                   command=self.filter_technologies).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="计算得分",
                   command=self.calculate_scores).pack(side=tk.LEFT, padx=5)

    def filter_technologies(self):
        # 获取选中的应用
        selected_apps = [app for app, var in self.app_vars if var.get()]

        if not selected_apps:
            messagebox.showwarning("警告", "请至少选择一个应用情境！")
            return

        # 筛选技术
        valid_tech = []
        for tech in self.technologies:
            if all(self.scores.loc[tech][app] > 0 for app in selected_apps):
                valid_tech.append(tech)

        # 清空旧输入
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        # 动态生成输入框
        ttk.Label(self.input_frame, text="技术名称").grid(row=0, column=0, padx=10)
        for col, app in enumerate(selected_apps, 1):
            ttk.Label(self.input_frame, text=app).grid(row=0, column=col, padx=10)

        self.time_entries = {}
        for row, tech in enumerate(valid_tech, 1):
            ttk.Label(self.input_frame, text=tech).grid(row=row, column=0, padx=10)
            self.time_entries[tech] = []
            for col in range(len(selected_apps)):
                entry = ttk.Entry(self.input_frame, width=8)
                entry.grid(row=row, column=col + 1, padx=10)
                self.time_entries[tech].append(entry)

    def calculate_scores(self):
        try:
            results = []
            selected_apps = [app for app, var in self.app_vars if var.get()]

            for tech, entries in self.time_entries.items():
                times = []
                for entry in entries:
                    time = float(entry.get())
                    if time < 0:
                        raise ValueError("时间不能为负数")
                    times.append(time)

                total_time = sum(times)
                if total_time <= 0:
                    raise ValueError("总时间必须大于0")

                weights = [t / total_time for t in times]
                scores = [self.scores.loc[tech][app] for app in selected_apps]
                combined = sum(s * w for s, w in zip(scores, weights))
                results.append((tech, combined))

            # 更新结果表格
            self.tree.delete(*self.tree.get_children())
            for tech, score in sorted(results, key=lambda x: -x[1]):
                self.tree.insert("", tk.END, text=tech, values=(f"{score:.2f}",))

        except Exception as e:
            messagebox.showerror("输入错误", f"数据验证失败：{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = EnergyStorageApp(root)
    root.mainloop()
