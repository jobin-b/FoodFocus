import React from "react";

type ProgBarProps = {
    percent: number,
    label: string
}

export default function ProgBar(props: ProgBarProps) {

    return (
        <div className="flex flex-col py-2">
            <p className="text-xl">{props.label}</p>
            <progress 
                className="rounded-md [&::-webkit-progress-value]:bg-orange-300 [&::-moz-progress-bar]:bg-orange-300"
                value={props.percent} />
        </div>
    )

}