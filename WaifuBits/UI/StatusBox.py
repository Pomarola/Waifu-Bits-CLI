import urwid
from datetime import date, timedelta
from collections import Counter

def ordinal(n):
    return f"{n}{'th' if 11<=n%100<=13 else {1:'st',2:'nd',3:'rd'}.get(n%10, 'th')}"

class StatusBox:
    def __init__(self):
        self.waifu_text = urwid.Text("", align='center')
        self.top_habits_text = urwid.Text("", align='center')
        self.bottom_habits_text = urwid.Text("", align='center')

        self.day_stats_text = urwid.Text("", align='center')
        self.week_stats_text = urwid.Text("", align='center')
        self.month_stats_text = urwid.Text("", align='center')

        self.trend_graph_text = urwid.Text("", align='center')
        self.streaks_text = urwid.Text("", align='center')

        column1 = urwid.Pile([
            ('pack', urwid.Divider()),
            ('weight', 1, urwid.AttrMap(urwid.LineBox(urwid.Filler(urwid.Padding(self.waifu_text, left=0, right=0), top=1, bottom=1), title="WAIFU", title_align='left'), 'unselected')),
            ('weight', 1, urwid.AttrMap(urwid.LineBox(urwid.Filler(urwid.Padding(self.top_habits_text, left=0, right=0), top=1, bottom=1), title="TOP 5 DONE", title_align='left'), 'unselected')),
            ('weight', 1, urwid.AttrMap(urwid.LineBox(urwid.Filler(urwid.Padding(self.bottom_habits_text, left=0, right=0), top=1, bottom=1), title="TOP 5 UNDONE", title_align='left'), 'unselected')),
            ('pack', urwid.Divider()),
        ])

        column2 = urwid.Pile([
            ('pack', urwid.Divider()),
            ('weight', 1, urwid.AttrMap(urwid.LineBox(urwid.Filler(urwid.Padding(self.day_stats_text, left=0, right=0), top=1, bottom=1), title="TODAY", title_align='left'), 'unselected')),
            ('weight', 1, urwid.AttrMap(urwid.LineBox(urwid.Filler(urwid.Padding(self.week_stats_text, left=0, right=0), top=1, bottom=1), title="LAST 7 DAYS", title_align='left'), 'unselected')),
            ('weight', 1, urwid.AttrMap(urwid.LineBox(urwid.Filler(urwid.Padding(self.month_stats_text, left=0, right=0), top=1, bottom=1), title="LAST 30 DAYS", title_align='left'), 'unselected')),
            ('pack', urwid.Divider()),
        ])

        column3 = urwid.Pile([
            ('pack', urwid.Divider()),
            ('weight', 1, urwid.AttrMap(urwid.LineBox(urwid.Filler(urwid.Padding(self.trend_graph_text, left=0, right=0), top=1, bottom=1), title="TREND PER DAY", title_align='left'), 'unselected')),
            ('weight', 1, urwid.AttrMap(urwid.LineBox(urwid.Filler(urwid.Padding(self.streaks_text, left=0, right=0), top=1, bottom=1), title="RECORDS", title_align='left'), 'unselected')),
            ('pack', urwid.Divider()),
        ])

        inner_columns = urwid.Columns([
            ('weight', 1, column1),
            ('weight', 1, column2),
            ('weight', 1, column3),
        ])
        padded_columns = urwid.Padding(inner_columns, left=2, right=2)
        self.view = urwid.AttrMap(urwid.LineBox(padded_columns, title="STATS"), 'bg')

    def _update_waifu_section(self, habits, statuses):
        completed = sum(1 for h in habits if (h, date.today()) in statuses and statuses[(h, date.today())])
        total = len(habits)
        rate = completed / total if total else 0

        thresholds = [0.2, 0.4, 0.6, 0.8, 1.0]
        labels = ["ANGRY", "MAD", "CURIOUS", "HAPPY", "ARARA", "WAIFU"]
        next_tier = next((t for t in thresholds if rate < t), 1.0)
        needed = int((next_tier * total) - completed + 0.9999)

        mode_index = sum(rate >= t for t in thresholds)
        mode = labels[mode_index]

        if mode == "ANGRY":
            waifu_msg = f"\nNino is FURIOUS! She's not even looking your way. Unforgivable!\n\n{needed} more to show her you care."
        elif mode == "MAD":
            waifu_msg = f"\nNino is MAD! You know you can do better... Baka!\n\n{needed} more to improve your score!"
        elif mode == "CURIOUS":
            waifu_msg = f"\nHmm... Nino is watching. Are you finally trying?\n\n{needed} more to impress her!"
        elif mode == "HAPPY":
            waifu_msg = f"\nYou're making Nino SMILE~ Keep it up!\n\n{needed} more for a special reaction!"
        elif mode == "ARARA":
            waifu_msg = f"\nArara~ Nino is pleasantly surprised. You’re doing well!\n\nJust {needed} more for the ultimate tier!"
        else:
            waifu_msg = f"\nNino is proud of you! WAIFU mode unlocked ❤️\n\nKeep being awesome!"

        self.waifu_text.set_text(waifu_msg)

    def _update_top_bottom_habits(self, habits, statuses):
        counter = Counter()
        undone = Counter()
        all_days = set(d for (_, d) in statuses if isinstance(d, date))
        for day in all_days:
            if any((habit, day) in statuses for habit in habits):
                for habit in habits:
                    if (habit, day) in statuses:
                        if statuses[(habit, day)]:
                            counter[habit] += 1
                        else:
                            undone[habit] += 1
                    else:
                        undone[habit] += 1

        top_done = counter.most_common(5)
        top_undone = undone.most_common(5)

        top_done_msg = "\n".join(f"{ordinal(i+1)} {habit.upper():<20}Times: {count:>3} [ + ]" for i, (habit, count) in enumerate(top_done))
        top_undone_msg = "\n".join(f"{ordinal(i+1)} {habit.upper():<20}Times: {count:>3} [ - ]" for i, (habit, count) in enumerate(top_undone))

        self.top_habits_text.set_text(top_done_msg)
        self.bottom_habits_text.set_text(top_undone_msg)

    def _update_range_stats(self, habits, statuses, today):
        def count_in_range(start, end):
            done = 0
            total = 0
            current = start
            while current <= end:
                for habit in habits:
                    total += 1
                    if (habit, current) in statuses and statuses[(habit, current)]:
                        done += 1
                    elif (habit, current) in statuses:
                        done += 0  # Explicit for clarity
                current += timedelta(days=1)
            return done, total

        completed = sum(
            1 for h in habits if (h, today) in statuses and statuses[(h, today)]
        )
        total = len(habits)
        rate = completed / total if total else 0

        weekday = today.weekday()
        weekday_name = today.strftime("%A")
        weekday_dates = set(
            k[1] for k in statuses
            if isinstance(k, tuple) and isinstance(k[1], date) and k[1].weekday() == weekday
        )

        weekday_done = 0
        weekday_total = 0
        for d in weekday_dates:
            for habit in habits:
                weekday_total += 1
                if (habit, d) in statuses:
                    if statuses[(habit, d)]:
                        weekday_done += 1
                else:
                    weekday_done += 0  # Explicit for clarity

        weekday_rate = weekday_done / weekday_total if weekday_total else 0

        self.day_stats_text.set_text(
            f"{'Habits Done:':<25}{completed:>5}\n"
            f"{'Habits Left:':<25}{total - completed:>5}\n"
            f"{'Completion Rate:':<25}{rate:>5.0%}\n"
            f"{f'Last {weekday_name}:':<25}" + f"{self._calculate_last_weekday_rate(habits, statuses, today):>5.0%}\n"
            f"{f'{weekday_name}\'s Avg:':<25}{weekday_rate:>5.0%}"
        )

        # WEEK STATS
        start_week = today - timedelta(days=today.weekday())
        week_done, week_total = count_in_range(start_week, today)
        week_rate = week_done / week_total if week_total else 0

        week_range_start = today - timedelta(days=7)
        week_range_done, week_range_total = count_in_range(week_range_start, today)
        week_range_rate = week_range_done / week_range_total if week_range_total else 0

        weekday_occurrences = [today - timedelta(days=i) for i in range(1, 8)]
        weekly_avg_done = 0
        weekly_avg_total = 0
        for d in weekday_occurrences:
            for habit in habits:
                weekly_avg_total += 1
                if (habit, d) in statuses:
                    if statuses[(habit, d)]:
                        weekly_avg_done += 1
                else:
                    weekly_avg_done += 0  # Explicit for clarity
        weekly_avg_rate = weekly_avg_done / weekly_avg_total if weekly_avg_total else 0

        self.week_stats_text.set_text(
            f"{'Habits Done:':<25}{week_done:>5}\n"
            f"{'Habits Left:':<25}{week_total - week_done:>5}\n"
            f"{'Completion Rate:':<25}{week_rate:>5.0%}\n"
            f"{'Last 7 Days Avg:':<25}{week_range_rate:>5.0%}\n"
            f"{'Weekly Avg:':<25}{weekly_avg_rate:>5.0%}"
        )

        # MONTH STATS
        start_month = today.replace(day=1)
        month_done, month_total = count_in_range(start_month, today)
        month_rate = month_done / month_total if month_total else 0

        month_range_start = today - timedelta(days=30)
        month_range_done, month_range_total = count_in_range(month_range_start, today)
        month_range_rate = month_range_done / month_range_total if month_range_total else 0

        monthly_avg_done = 0
        monthly_avg_total = 0
        for i in range(1, 31):
            d = today - timedelta(days=i)
            for habit in habits:
                monthly_avg_total += 1
                if (habit, d) in statuses:
                    if statuses[(habit, d)]:
                        monthly_avg_done += 1
                else:
                    monthly_avg_done += 0  # Explicit for clarity
        monthly_avg_rate = monthly_avg_done / monthly_avg_total if monthly_avg_total else 0

        self.month_stats_text.set_text(
            f"{'Habits Done:':<25}{month_done:>5}\n"
            f"{'Habits Left:':<25}{month_total - month_done:>5}\n"
            f"{'Completion Rate:':<25}{month_rate:>5.0%}\n"
            f"{'Last 30 Days Avg:':<25}{month_range_rate:>5.0%}\n"
            f"{'Monthly Avg:':<25}{monthly_avg_rate:>5.0%}"
        )

        # TREND PER DAY
        weekday_stats = []
        for i in range(7):
            weekday_name = (date(2023, 1, 2) + timedelta(days=i)).strftime('%A')
            dates = []
            for offset in range(60):
                d = today - timedelta(days=offset)
                if d.weekday() == i and any((h, d) in statuses for h in habits):
                    dates.append(d)
            day_done = 0
            day_total = 0
            for d in dates:
                for habit in habits:
                    day_total += 1
                    if (habit, d) in statuses:
                        if statuses[(habit, d)]:
                            day_done += 1
                    else:
                        day_done += 0  # Explicit for clarity
            rate = day_done / day_total if day_total else 0
            bar = "█" * int(rate * 20)
            weekday_stats.append(f"{weekday_name:<15}{bar:<25} {rate:5.0%}")

        self.trend_graph_text.set_text("\n".join(weekday_stats))

    def _update_streaks_section(self, habits, statuses, today):
        streaks = {
            "You gave it all for her": 0,    # 100%
            "You were a good husbando": 0,            # > 75%
            "You made her happy": 0,         # > 50%
            "She was disappointed": 0,         # > 25%
            "She was pissed": 0,             # > 0% and < 50%
            "She was angry": 0,              # > 0% and < 25%
            "You were garbage": 0                     # 0%
        }

        labels = list(streaks.keys())
        current = today
        max_days = 100  # Limit to avoid infinite loops

        while max_days > 0:
            if not any((h, current) in statuses for h in habits):
                break

            total = len(habits)
            done = 0
            for habit in habits:
                if (habit, current) in statuses and statuses[(habit, current)]:
                    done += 1
            rate = done / total if total else 0

            if rate == 1.0:
                label = labels[0]
            elif rate > 0.8:
                label = labels[1]
            elif rate > 0.6:
                label = labels[2]
            elif rate > 0.4:
                label = labels[3]
            elif rate > 0.2:
                label = labels[4]
            elif rate > 0.0:
                label = labels[5]
            else:
                label = labels[6]

            streaks[label] += 1
            current -= timedelta(days=1)
            max_days -= 1

        streaks_msg = "\n".join(f"{label:<35} for {days} days" for label, days in streaks.items())
        self.streaks_text.set_text(streaks_msg)

    def _calculate_last_weekday_rate(self, habits, statuses, today):
        previous = today - timedelta(days=7)
        same_weekday = previous
        done = 0
        total = 0
        for habit in habits:
            total += 1
            if (habit, same_weekday) in statuses and statuses[(habit, same_weekday)]:
                done += 1
            else:
                done += 0  # Explicit for clarity
        return done / total if total else 0

    def set_data(self, habits, statuses):
        today = date.today()
        self._update_waifu_section(habits, statuses)
        self._update_top_bottom_habits(habits, statuses)
        self._update_range_stats(habits, statuses, today)
        self._update_streaks_section(habits, statuses, today)