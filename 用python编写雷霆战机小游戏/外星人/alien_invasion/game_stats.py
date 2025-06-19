import json

class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings=ai_settings
        self.reset_stats()
        #最高分，任何情况下不重置
        self.high_score=self._load_high_score()

        self.game_active=False

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1
        self.ammo=2

    def _load_high_score(self):
        """从文件中加载最高分"""
        try:
            #with open(file)是常用的打开文件的方式，并可以自动关闭
            with open('high_score.json') as f:
                #json.load(fp)	从 文件对象 读取 JSON 数据 → Python 对象
                return int(json.load(f))
        except (FileNotFoundError,json.JSONDecodeError):
            return 0
    def _save_high_score(self):
        """将最高分保存在文件"""
        with open('high_score.json','w') as f:
            #json.dump(obj, fp)	将 Python 对象写入 文件（转换为 JSON）
            json.dump(self.high_score,f)


