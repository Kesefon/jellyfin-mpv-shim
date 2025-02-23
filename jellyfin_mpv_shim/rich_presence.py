from pypresence import Client
import time

client_id = "743296148592263240"
RPC = Client(client_id)
RPC.start()


def register_join_event(syncplay_join_group: callable):
    RPC.register_event('activity_join', syncplay_join_group)


def send_presence(
    title: str,
    subtitle: str,
    playback_time: float = None,
    duration: float = None,
    playing: bool = False,
    syncplay_group: str = None,
):
    small_image = "play-dark3" if playing else None
    start = None
    end = None
    if playback_time is not None and duration is not None and playing:
        start = int(time.time() - playback_time)
        end = int(start + duration)
    RPC.set_activity(
        state=subtitle,
        details=title,
        instance=False,
        large_image="jellyfin2",
        start=start,
        end=end,
        large_text="Jellyfin",
        small_image=small_image,
        party_id=str(hash(syncplay_group)),
        party_size=[1, 100],
        join=syncplay_group,
    )


def clear_presence():
    RPC.clear_activity()
