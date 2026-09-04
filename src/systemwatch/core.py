from collections.abc import Mapping

def diff(previous: Mapping[str, object], current: Mapping[str, object]) -> dict[str,list[str]]:
    old,new=set(previous),set(current)
    return {"added":sorted(new-old),"removed":sorted(old-new),"changed":sorted(k for k in old&new if previous[k]!=current[k])}
