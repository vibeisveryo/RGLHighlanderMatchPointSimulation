from division import Division

my_list = ["a", "b", "c", "d", "e", "f", "g", "h"]

invite = Division(name="Invite", team_list=None, no_of_teams=8, skill_style=1)
invite.rr_run_matches()
print(invite)