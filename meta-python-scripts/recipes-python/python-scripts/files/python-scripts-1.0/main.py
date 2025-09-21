#!/usr/bin/env python3

# Filename: main.py
# Author: Nagel Mejía Segura
# Created: 2025-09-10
# Description: This script processes a video file, gets video with Gstreamer and applies a box detection.

import sys
import cv2
import numpy as np
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
from src.detector import Detector
import os

Gst.init(None)

def make_pipeline(path):
    pipeline_desc = (
        f"filesrc location=\"{path}\" ! qtdemux name=demux "
        "demux.video_0 ! h264parse ! avdec_h264 ! videoconvert ! "
        "video/x-raw,format=BGRx ! "
        "appsink name=appsink emit-signals=true max-buffers=1 drop=true"
    )
    return Gst.parse_launch(pipeline_desc)

def get_process_frame(pipeline):
    appsink = pipeline.get_by_name('appsink')
    pipeline.set_state(Gst.State.PLAYING)

    try:
        while True:
            sample = appsink.emit("pull-sample")
            if sample is None:
                bus = pipeline.get_bus()
                msg = bus.timed_pop_filtered(0, Gst.MessageType.EOS | Gst.MessageType.ERROR)
                if msg:
                    if msg.type == Gst.MessageType.EOS:
                        print("End of stream")
                        break
                    elif msg.type == Gst.MessageType.ERROR:
                        err, debug = msg.parse_error()
                        print("GStreamer error:", err, debug)
                        break
                continue

            buf = sample.get_buffer()
            caps = sample.get_caps()
            s = caps.get_structure(0)
            width = s.get_value('width')
            height = s.get_value('height')

            success, mapinfo = buf.map(Gst.MapFlags.READ)
            if not success:
                continue
            try:
                arr = np.frombuffer(mapinfo.data, dtype=np.uint8)
                frame = arr.reshape((height, -1, 4))[:, :width, :3].copy()

                detector = Detector()

                result_frame, edges, _ = detector.process_frame(frame)

                cv2.imshow('Edges',edges)
                cv2.imshow("Detection", result_frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q') or key == 27:
                    print("Usuario pidió salir")
                    break

            finally:
                buf.unmap(mapinfo)

    finally:
        pipeline.set_state(Gst.State.NULL)
        cv2.destroyAllWindows()

def main():
    # Default path
    DEFAULT_PATH = "./inputs/box_test.mp4"
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PATH


    if not os.path.isfile(path):
        print(f"Error: el archivo '{path}' no existe")
        sys.exit(1)

    pipeline = make_pipeline(path)
    get_process_frame(pipeline)

if __name__ == "__main__":
    main()