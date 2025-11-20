// types.ts
export interface ScriptOptions {
  scriptName: string;
  environment: string;
  verbose: boolean;
}

export interface DeploymentConfig {
  scripts: ScriptOptions[];
  deploymentTargets: string[];
}

export interface DeploymentTarget {
  name: string;
  url: string;
  credentials: {
    username: string;
    password: string;
  };
}

export enum Environment {
  DEV = 'dev',
  PROD = 'prod',
  STG = 'stg',
}

export interface ScriptResult {
  scriptName: string;
  success: boolean;
  output: string;
  error: string | null;
}