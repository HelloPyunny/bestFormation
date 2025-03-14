# formation.py

class FormationStrategy:
    def apply_tactics(self):
        raise NotImplementedError("이 메서드는 서브클래스에서 구현해야 합니다.")

class Balanced442(FormationStrategy):
    def apply_tactics(self):
        return "공격과 수비의 균형 유지, 중앙 미드필더의 볼 배급 중요"

class Attacking433(FormationStrategy):
    def apply_tactics(self):
        return "측면 공격 강화, 윙어와 풀백의 오버래핑 필수"

class Modern4231(FormationStrategy):
    def apply_tactics(self):
        return "AMC 중심 전술, 중앙에서 창의적인 패스 플레이 필요"

class Defensive532(FormationStrategy):
    def apply_tactics(self):
        return "두터운 수비라인, 빠른 역습 활용"

class ExtremeDefensive541(FormationStrategy):
    def apply_tactics(self):
        return "수비 집중, 상대 공격 차단 후 롱볼 역습"

class Aggressive4141(FormationStrategy):
    def apply_tactics(self):
        return "공격형 미드필더 전진 배치, 수비형 미드필더가 중심 역할"

class Brazilian4222(FormationStrategy):
    def apply_tactics(self):
        return "창의적인 미드필더 활용, 공격적인 패스 플레이"

class CentralAttack4312(FormationStrategy):
    def apply_tactics(self):
        return "중앙 공격 집중, AMC를 통한 기회 창출"


formation_tactics = {
    "4-4-2": Balanced442(),
    "4-3-3": Attacking433(),
    "4-2-3-1": Modern4231(),
    "3-5-2": Balanced442(),
    "3-4-3": Attacking433(),
    "5-3-2": Defensive532(),
    "5-4-1": ExtremeDefensive541(),
    "4-1-4-1": Aggressive4141(),
    "4-2-2-2": Brazilian4222(),
    "4-3-1-2": CentralAttack4312()
}

def get_tactics(formation):
    strategy = formation_tactics.get(formation)
    if strategy:
        return strategy.apply_tactics()
    else:
        return "해당 포메이션에 대한 전술 정보가 없습니다."

if __name__ == "__main__":
    user_formation = input("포메이션을 입력하세요 (예: 4-4-2): ")
    print(get_tactics(user_formation))
